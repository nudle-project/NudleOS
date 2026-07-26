import random
import time
class word_list:
        words = ["rosecrans", "sacramento", "santa monica", "san diego", "san francisco", "san jose", "san luis obispo", "santa barbara", "santa clarita", "santa cruz", "santa fe", "santa rosa", "santa ynez", "santa maria", "santa monica mountains", "santa monica pier", "santa monica beach", "santa monica boulevard", "santa monica freeway", "moscow", "moscow mule", "moscow state university", "moscow river", "moscow oblast", "moscow kremlin", "moscow metro", "moscow zoo", "moscow circus", "moscow ballet", "moscow art museum", "moscow state circus", "moscow state university of civil engineering", "moscow state university of medicine and dentistry", "moscow state university of economics, statistics and informatics", "moscow state university of railway engineering", "moscow state university of printing arts", "moscow state university of technology and management", "moscow state university of transport", "moscow state university of telecommunications", "moscow state university of tourism and service", "moscow state university of physical culture", "moscow state university of psychology and education", "moscow state university of social sciences", "moscow state university of law", "moscow state university of international relations", "moscow state university of economics, statistics and informatics", "moscow state university of civil engineering", "moscow state university of medicine and dentistry", "moscow state university of economics, statistics and informatics", "mumbai", "mumbai city", "mumbai airport", "mumbai metro", "mumbai university", "mumbai police", "mumbai stock exchange", "mumbai port", "mumbai railway station", "mumbai central", "mumbai suburban railway", "mumbai local train", "mumbai monorail", "mumbai bus rapid transit system", "mumbai international airport", "mumbai domestic airport", "mumbai city district", "mumbai city corporation", "mumbai city police", "mumbai city railway station"]
        ### words must bespelled correctly and be in the list of words when displayed to the user. The user must type the word correctly to get a point. The words are randomly selected from the list of words and displayed to the user one at a time. The user has 10 seconds to type the word correctly. If the user types the word correctly, they get a point and the next word is displayed. If the user types the word incorrectly or does not type the word within 10 seconds, they do not get a point and the next word is displayed. The game continues until the user decides to quit. The user's score is displayed at the end of the game.
        print("Type the following word:")
        word = random.choice(words)
        print(word)
        puts=input("Type the word: ")
        print("You typed: " + puts)
        if puts == word:
            print("Correct!")
        else:
            print("Incorrect!")
        #Something needed to fix: Make it repeat the process of displaying a word, getting user input, and checking if the input is correct until the user decides to quit. Also, implement a timer to limit the time for typing the word to 10 seconds.
        
