-------------------------------------------------------------------------------------------------------------------------------
Nick Derf(ND)

Neurogammon

Brief:
	Written in python
	5 files so far:
	
		Neurogammon.py - the main file that is responsible for having the Network interact with the Game.
						Will also handle results and analysis
						
		TDGammon.py - Wrapper for the network. Handles all network related activities such as formulating the correct network weights and analyzing current board states 
		
		Game.py - Class Wrapper for backgammon-related activities. Handles gameplay functions.
		
		Checker.py - Class wrapper for one checker piece for backgammon
		
		Player.py - Class wrapper for one player
		
		
Process:
	I have done some initial coding for each of these files, setting up basic classes, functions, and attributes that I think will be needed. My main goal was to make it clear what the process should be moving forward.
	
	Essentially the workflow ends up looking something like this:
	1. Initialize Game and Network (Neurogammon.py)
	2. The train function is now called and begins our main loop (Neurogammon.py)
	3. Given an initial amount of iterations; games to play, start a game of backgammon.
	4. Have 2 players go back and forth choosing moves. We need to calculate all possible states first before the network analyzes.
	5. Now we analyze the list of states that we have generated. We are essentially calclating the probability that we can win from this state. We can use the "White-Checkered" player as the one we want to maximize probability and the "Black-Checkered" player as the player want to minimize probability or vice-versa, it doesn't matter. 
	6. Continue 4-5 until a winner has been declared.
	7. Once a winner has been declared, we need have the agent learn from the game and adjust its weights 
	8. ANALYSIS can be done du
	
	NOTES:
	** Steps 4 and 5 are going to be the beefiest to make, there is a lot that goes on here. They will require that all objects be in play at some point
	**By no means does my code have stay the way it is, functions can be deleted and created as needed.
	
	**Since we are striving towards having a good report to turn, whether we are able to get this to work completely shouldn't effect the quality of the report. I think we will have plenty to go off of still for the final report, no matter our outcome.
	
	SOURCES:
	There are 2 sources that I mainly used for this
	https://bkgm.com/articles/tesauro/ProgrammingBackgammon.pdf - an article. I have the downloaded PDF that is uploaded to github and is called "NeurogammonSummary.pdf"
	https://github.com/millerm/TD-Gammon - an attempt from someone else trying to the same thing we are. I tried running their program and it took a very long time to run as well as after 30 tries, it didn't seem to "doing" better when playing. This code has also been downloaded and placed in the "Example" folder

Google Doc: 
<ul><li>https://docs.google.com/document/d/10SMnKHj9104LGmn_yrMJarUTjCsJzLMgbnhYNcaRkis/edit?usp=sharing</li></ul>

--------------------------------------------------------------------------------------------------------------------------------	
