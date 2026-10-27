# tic-tac-toe-ai-v2_HackClub
A terminal version of tic tac toe with som AI too

The program starts by giving the user five options on what player 'X' and player 'O' could be.   
The player can either choose human, dumb-bot, smart-bot, genius-bot, or god-bot. It then    
takes those options and makes a game where the two players play each other. A user can put AI's against   
each other, play against AI's, or play against their friend, if they have one.

### Modes
- Human: Asks user for y,x coordinate on the tic tac toe board to play.
- Dumb-bot: Finds all squares that aren't taken and randomly decides on one to move.
- Smart-bot: Same as dumb-bot but if bot is one away from winning it finds and executes the winning move.
- Genius-bot: Same as smart-bot but if opponent is one away from winning, the bot blocks opponent.
- God-bot: Find and branches out all possible moves from a point and does the best one.

## EXAMPLE
'X' as human    
'O' as god-bot   
<img src="https://imgur.com/5kxToap.jpg" width="800">

## How to Run
#### (This has only been tested on a Mac so instructions are only for Mac)
1. Download the most recent executable from the [releases page](https://github.com/hardeek-sharma/tic-tac-toe-ai-v2_HackClub/releases)
2. Open up Terminal.app and cd to where the file is downloaded
3. type "chmod +x " and drag the executable over to the terminal line so it auto fills in its path
4. The terminal thing might look like this: chmod +x /Users/name/Downloads/main
5. Type ./main in the terminal and now the program works
6. only step 5 is needed to use the program again