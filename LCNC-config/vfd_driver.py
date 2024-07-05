import minimalmodbus
import time
import linuxcnc
import hal
import serial

# Initialize the Modbus connection
def initialize_vfd():
    try:
        vfd = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # Port name, slave address
        vfd.serial.baudrate = 9600
        vfd.serial.bytesize = 8
        vfd.serial.parity = serial.PARITY_NONE
        vfd.serial.stopbits = 1
        vfd.serial.timeout = 1
        return vfd
    except Exception as e:
        print("Failed to initialize VFD: {}".format(e))
        return None

vfd = initialize_vfd()
max_rpm = 18000
max_freq = 300

# HAL component
h = hal.component("vfd")
h.newpin("spindle-on", hal.HAL_BIT, hal.HAL_IN)
h.newpin("spindle-cw", hal.HAL_BIT, hal.HAL_IN)
h.newpin("spindle-ccw", hal.HAL_BIT, hal.HAL_IN)
h.newpin("spindle-speed", hal.HAL_FLOAT, hal.HAL_IN)
h.newpin("spindle-on-fault", hal.HAL_BIT, hal.HAL_OUT)
h.newpin("spindle-voltage", hal.HAL_FLOAT, hal.HAL_OUT)
h.newpin("spindle-current", hal.HAL_FLOAT, hal.HAL_OUT)
h.newpin("spindle-power", hal.HAL_FLOAT, hal.HAL_OUT)
h.newpin("spindle-torque", hal.HAL_FLOAT, hal.HAL_OUT)
h.newpin("spindle-running_speed", hal.HAL_FLOAT, hal.HAL_OUT)
h.newpin("spindle-fault", hal.HAL_U32, hal.HAL_OUT)
h.newpin("spindle-rps", hal.HAL_FLOAT, hal.HAL_OUT)
h.newpin("spindle-at-speed", hal.HAL_BIT, hal.HAL_OUT)
h.newpin("connection", hal.HAL_BIT, hal.HAL_OUT)
h.ready()

def rpm_to_perc(rpm):
    if abs(rpm) > max_rpm:
        return 0
    return abs(rpm / max_rpm)

def spindle_at_speed(set_rpm, current_rpm, variance):
    if current_rpm < set_rpm - variance or current_rpm > set_rpm + variance:
        return 0
    else:
        return 1

while True:
    try:
        if not vfd:
            vfd = initialize_vfd()
            if not vfd:
                time.sleep(1)
                continue

        time.sleep(0.01)
        #-----------------SPINDLE VFD--------------------
        set_freq = vfd.read_register(0x3001) / 100
        voltage = vfd.read_register(0x3003)
        current = vfd.read_register(0x3004) / 100
        power = vfd.read_register(0x3005)
        torque = vfd.read_register(0x3006)
        fault = vfd.read_register(0x8000)

        h['spindle-running_speed'] = set_freq / max_freq * max_rpm
        h['spindle-rps'] = set_freq / max_freq * max_rpm/60
        h['spindle-voltage'] = voltage
        h['spindle-current'] = current
        h['spindle-power'] = power
        h['spindle-torque'] = torque
        h['spindle-fault'] = fault

        if h['spindle-fault'] != 0:
            h['spindle-on-fault'] = True

        if h['spindle-on']:
            if h['spindle-cw']:
                vfd.write_register(0x1000, 1, 0, 6)
            if h['spindle-ccw']:
                vfd.write_register(0x1000, 2, 0, 6)
        else:
            vfd.write_register(0x1000, 6, 0, 6)

        vfd.write_register(0x3000, rpm_to_perc(h['spindle-speed']) * 10000, 0, 6)
        h['spindle-at-speed'] = spindle_at_speed(h['spindle-speed'], set_freq / max_freq * max_rpm, 100)
        h['connection'] = True  # Set communication status to true if no exceptions are raised

    except (minimalmodbus.NoResponseError, minimalmodbus.InvalidResponseError, 
            minimalmodbus.SlaveReportedException, serial.SerialException) as e:
        print("Communication error: {}".format(e))
        h['connection'] = False  # Set communication status to false if an error occurs
        vfd = None  # Reset vfd to trigger reconnection in the next loop
        time.sleep(1)
    except minimalmodbus.ModbusException as e:
        print("Modbus error: {}".format(e))
        h['connection'] = False  # Set communication status to false if an error occurs
        vfd = None  # Reset vfd to trigger reconnection in the next loop
        time.sleep(1)
    except Exception as e:
        print("Unexpected error: {}".format(e))
        h['connection'] = False  # Set communication status to false if an error occurs
        vfd = None  # Reset vfd to trigger reconnection in the next loop
        time.sleep(1)
    except KeyboardInterrupt:
        raise SystemExit
