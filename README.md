# MyHeavyNC
My redesigned printNC, idk how to call it to be fair, input is welcome!

First and foremost I AM NOT AN ENGINEER, I'm a theoretical physicist who tried to be an automation engineer but got rejected by admission exams, so there will be errors and things could have surely been done better.

With this said, the file structure is pretty self-explanatory.
In the LCNC-config folder there is all you need to copy and paste into ~/linuxcnc/config for it to work.
Inside said folder there is also a new rewritten post processor to work with my cooling setup and more importantly Fusion360 probing routines that have also been partially rewritten.
Another thing I hated was how tool-lenght-offsets were calculated in the M6remap macro, so I re-wrote them too, now you just need to touch-off the spindle cone and write it into the .ini.
On this line of reasonning there wasnt any necessity for me to use the touchoff procedure used by QtDragon, as such I took the occasion to rewire the button to the M6 command.

Why chosing this project tho you may wonder, and thats easy, it took everything good there is with the original PrintNC project, and made it stiffer, heavier and more powerfull. The result is comfortably milling at 60+ cm3/min in aluminum and the ability to cut steel at 6krpm.
You can check the performance of the machine out by looking at my IG profile


# MyHeavyNC

Welcome to MyHeavyNC, a redesigned version of PrintNC. I'm open to suggestions and feedback on the project!

## About

First and foremost, I am **NOT** an engineer. I am a theoretical physicist who attempted to become an automation engineer but was unsuccessful in admission exams. As a result, there may be errors and areas for improvement in this project.

## File Structure and Features

The file structure is straightforward. In the `LCNC-config` folder, you will find everything you need to copy and paste into `~/linuxcnc/config` to get it working. This folder also contains a rewritten post processor for my cooling setup and partially rewritten Fusion360 probing routines.
Another thing I didnt like how it was handled was tool-lenght-offsets and so I rewrote `M6remap` macro. Now, you only need to touch off the spindle cone on the tool setter and write the absolute measurement into the `.ini` file.
Because of this I found no necessity to use the touchoff procedure used by QtDragon, so I rewired the button to the `M6` command.

## Why Choose This Project?

MyHeavyNC takes everything good from the original PrintNC project and makes it stiffer, heavier, and more powerful. The result is the ability to mill at 60+ cm³/min in aluminum and cut steel at 6000 rpm.
You can check out the performance of the machine on my [Instagram profile](https://www.instagram.com/diymachining/).

## Interesting details
1. I used a UHPC mix specifically made to anchor down machines that produce a lot of vibrations, it's also water and oil resistant. The company that makes it its called Draco and the product is Flueco 75 if you wish to give a look at the datasheet.
2. The VFD I use is a really important component imo, I recently bought a Folinn BD600 with SVC. I had to sacrifice some top end as it has a maximum output frequency of 300hz in SVC but i gained a lot of torque everywhere in the rpm range. It's a bit more expensive but it makes a night and day difference.

