# MyHeavyNC

Welcome to MyHeavyNC, a redesigned version of PrintNC. I'm open to suggestions and feedback on the project!

## About

First and foremost, I am **NOT** an engineer. I am a theoretical physicist who attempted to become an automation engineer but was unsuccessful in admission exams. As a result, there may be errors and areas for improvement in this project.

## File Structure and Features

The file structure is straightforward. In the `LCNC-config` folder, you will find everything you need to copy and paste into `~/linuxcnc/config` to get it working. This folder also contains a rewritten post processor for my cooling setup and partially rewritten Fusion360 probing routines.
Another thing I didn't like about how it was handled was tool-length-offsets and so I modifyed `M6remap` macro. Now, you only need to touch off the spindle cone on the tool setter and write the absolute measurement into the `.ini` file.
Because of this, I found no necessity to use the touchoff procedure used by QtDragon, so I rewired the button to the `M6` command.

To install in LinuxCNC all the above additions:
1. copy the `m6-remap` folder into ~/linuxcnc/nc_files/examples/
2. copy `f360-subroutines` into \~/linuxcnc/nc_files/examples
3. import in Fusion the new post processor `LCNC.cps`

## Why Choose This Project?

MyHeavyNC takes everything good from the original PrintNC project and makes it stiffer, heavier, and more powerful. The result is the ability to mill up to 100 cm³/min in aluminium and cut steel at 6000 rpm.
You can check out the performance of the machine on my [Instagram profile](https://www.instagram.com/diymachining/).

## Interesting details
1. I used a UHPC mix specifically made to anchor down machines that produce a lot of vibrations, it's also water and oil-resistant. The company that makes it is called Draco and the product is Flueco 75 if you wish to give a look at the datasheet.
2. The VFD I use is a really important component imo, I recently bought a Folinn BD600 with SVC. I had to sacrifice some top end as it has a maximum output frequency of 300hz in SVC but I gained a lot of torque everywhere in the rpm range. It's a bit more expensive but it makes a night and day difference.

