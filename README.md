# python-turtle-crossing
Welcome!

My turtle crossing game deviates from the Udemy mechanics as a challenge.

Original Udemy mechanics:
- The player begins at pos(0,-280) which is at the bottom of the screen
- The player's challenge is to be able to reach the top of the screen where y = 280
- Afterwards, the level goes up by simply increasing the speed of the cars going by

My mechanics:
- The player begins at pos(0,0)
- The player will have to play frogger and avoid getting hit
- The finish line is only established when the first car finally covers an X-DISTANCE

Difficulty upgrade for each level:
- The X-DISTANCE increases by a factor of 1.5 for each level, i.e., if the first car has to cover 1200px,
    it will now cover 1800px
- The NUMBER OF CARS generated increases. The probability of car generation for each level goes up by 10% each time
- The SPEED of the cars passing by increases by 10 (same as the original mechanics)