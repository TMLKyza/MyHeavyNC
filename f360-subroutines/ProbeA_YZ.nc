(do this in metric)
G21

(Probing control variables)
#<_probeFastSpeed>= 762.
#<_probeSlowSpeed>= 50.8
#<_probeSlowDistance>= 1.016

(select the correct wcs for rotary work)
G54.1 P100

(we will need to know the accurate - tool table - tip radius)
o<f360_tip_radius> call
#<tip_radius> = #<_value>

(clearance set to 10mm)
#<clearance> = 10.0
#<feed> = 1500

(start at y 0)
G90
G1 Y0.0 F#<feed>
G0 A0.0

(probe down to the first touch)
o<f360_probe_z> call [-1.] [#<clearance>]

(and record the z coord)
#<zhit> = #5063

(Retract above the hit)
G90 G1 Z[#<zhit> + 2.0 * #<clearance>] F#<feed>
(DEBUG,Z touch found at #<zhit>)

(now rotate and do the -ve y)
G0 A90.0

(move across)
o<f360_safe_move_y> call [-#<zhit> - #<clearance> - #<tip_radius>] [#<feed>]

(move down)
G90
G38.3 Z[-#<tip_radius>]

(then probe in +y direction)
o<f360_probe_y> call [1.0] [#<clearance> * 2.0]
#<yhit1> = [#5062 + #<tip_radius>]
(and retract)
G91 G1 Y[-#<clearance>] F#<feed>
(DEBUG,-ve y touch detected at #<yhit1>)

(move up to clearance height)
G90 G1 Z[#<zhit> + 2.0 * #<clearance>] F#<feed>
(back to the centre)
G1 Y0 A0.0

(then move for +ve y probe)
G0 A-90.0

(move across)
o<f360_safe_move_y> call [#<zhit> + #<clearance> + #<tip_radius>] [#<feed>]

(move down)
G90
G38.3 Z[-#<tip_radius>]

(then probe in -y direction)
o<f360_probe_y> call [-1.0] [#<clearance> * 2.0]
#<yhit2> = [#5062 - #<tip_radius>]
(and retract)
G91 G1 Y#<clearance> F#<feed>
(DEBUG,+ve y touch detected at #<yhit2>)

(move up to clearance height)
G90 G1 Z[#<zhit> + #<clearance>] F#<feed>
(back to the centre)
G1 Y0 A0.0

(now apply the corrections)
o<f360_update_y> call [0.0] [[#<yhit1> + #<yhit2>] / 2.0] [0.0]
o<f360_update_z> call [0.0] [#<zhit>] [[#<yhit2> - #<yhit1>] / 2.0]

(end of program)
G90
M30
