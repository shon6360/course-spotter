# Course Sniper
Really more of a course "spotter" than a sniper, a sniper takes the shot, which in this case would be registering for the class but doing so could result in a ban from WebReg usage which is not a risk I'm willing to take (yet). It's more of a spotter because it points out the open sections for you to grab, not unlike a spotter pointing out targets for a sniper.

## Introduction
After doing 0 research and 0 testing, I came to the conclusion that all other sniping bots are inherently worse than anything I could ever make myself. For that reason, I have made my own course openning notification bot (since sniping bots can never truly snipe classes, just notify you as to when courses open, thus making them more of a spotter?) which will tell me when the courses I require are open. 


## The Main Ideas
For now, the project is written in Python. It uses requests to get class data from the Schedule of Classes (SoC) API and uses a Discord Webhook as an output.

The SoC API provides two .json files, allCourses and openSection. The allCourses.json file is essentially a very long multidimensional array/hashmap with all the data you can imagine about courses inside. Courses in this file are sorted by "subject" then "courseNumber". The openSections.json file contains a sorted list of class "indexes", the unique identifier for courses, and nothing else. 

The vision from here is to have users input the courses using the "courseString", find these courses in allCourses.json, pull the relevant data such as the "index" and essentially cache it, then every interval update openSections.json and binary search for all the indexes cached and if it appears we can output to the Discord the relevant data such as their ability to register in this course and maybe even later down the line which classes they should drop to fit.

But currently the project is in a very rough prototype phase where I'm just trying to get basic core functionality working reliably, accurately, and in a way that lays the foundations for things to come. This has been moderately difficult due to a lack of proper documentation however other course snipers on GitHub have been an invaluable resource for examples and explainations. 

My goal more than anything is get in practice writing cleaner and more organized code, school has taught me to write code with the goal of getting an assignment done but I want to make my code more sustainable.

## The Roadmap
- Basic features/round out the prototype
- Ensure the accuracy, there were problems in previous prototypes where frequent false positives were given
- Implement search algorithm
- Transition this to a language that is not horribly slow python. I'm thinking C because that could be fun 
- Ability to live update the sniping list without downtime
- Seamless multiple users integration
- Smart reccomendations on classes to be dropped to fit
