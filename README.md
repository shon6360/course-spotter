After doing 0 research and 0 testing, I came to the conclusion that all other sniping bots are inherently worse than anything I could ever make myself. For that reason, I have made my own course openning notification bot (since sniping bots can never truly snipe classes, just notify you as to when courses open, thus making them more of a spotter?) which will tell me when the courses I require are open. 

For now, written in python and uses requests to get the info from SoC then requests to send a message to my discord server.


For the future, I want to:
- Live update the sniping list without downtime
- Remove errors from the API (sometimes there are false positives, implying there may also be false negatives that go undetected)
- Allow for multiple users


But currently the project is in a very rought prototype phase where I'm just trying to get basic core functionality working reliably and accurately. From here, I want to add basic features, improve search algorithms, and transition this to a language that is not horribly slow python. I'm thinking C because that could be fun. 
