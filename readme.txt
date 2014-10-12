BunnyDefender v0.99
Edited/Updated by David Levy - dtlevy@gmail.com
Oct 14, 2014
Based on the tutorial found: http://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python

============================================================================================================================================

|Menu|
======
Controls:	-W, A or UP/Down Arrow: Navigate
		-Enter or Return: Select Option
		-Escape: Quit program


|Gameplay|
==========
Controls:	-F6: Toggle Cursor Window Lock
		-WSAD or Arrow Keys: Up, Down, Left, Right
		-Mouse cursor: aim weapon.
		-Escape: End game
			
Firing:		-Carrot: Mouse buttons - Scroll wheel for rapid fire.
		-Nuke: Spacebar or Numpad0 .
			
Enemies: 	If player collides with any enemy one heart will be lost.
		-Normal Grey 	- 25 base damage - Nukes don't 'die' to normal enemies but still enemies die (Can kill >1 with one nuke).
		-Evil(fast) Red	- 50 base damage - Immune to carrots (Carrots pass through evils, must use one nuke per evil).
		-Arrows

Pickups: 	-Hearts: Gain 1 heart for each heart you touch.
		-Nukes: Gain 3 nukes for each nuke you touch.
			
Scoring:	The following will factor into your final score when the game ends:
		-Enemies Killed
		-Accuracy
		-Base Health
		-Hearts
		-Nukes

Config:		Feel free to edit the config.cfg (found in resources folder) file as follows:
		-Line 1: Initial Game Timer 
		-Line 2: Initial # of Nukes - Max 99
		-Line 3: Initial # of Hearts - Max 12			
============================================================================================================================================			
			
Please try to BREAK the game.(find bugs) - Hit Detection is not perfect
Also any suggestions are very welcome even if they are things that change the game completely.

Protips: -The game doesn't end until the last enemy is killed...
	 -Line up nukes to take out multiple grey enemies and improve accuracy.
