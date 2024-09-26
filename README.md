# PokerTracker
#### Video Demo:  https://youtu.be/m9lGyIbGELo?si=GkCqXuyN9GkgCU_Z
#### Description:
>I wonder how I could keep track of my money while playing poker with my friends

That's where my program comes in, PokerTracker™.
I made this since ~~I love gambli*ng so much~~ I wanted to play poker with my friend, but we had no way to keep count of our money.
Sure, we could have used a pen and paper, but that wasn't good enough, and we would have needed to maintain multiple sheets for each of our banks as well as the pot.
**OR** I could spend basically close to a week on making a program whose **ONLY** purpose is to keep track of the money. I noticed slowly over the course of the making of PokerTracker™, that I'm at this point basically making a poker app without the cards. Which was a bit disappointing since I thought I was making something groundbreaking, but whatever, I'm here already. ~~google sunk cost fallacy~~
It first started as a complete bare bones just having bank accounts for each of the players, you couldn't even give the players names. It was just Player1, Player2 and so on. With that, there was just a pot. Thats all that there was. You could choose "Put Money in Pot" or "Give Pot to Player" or "Next Player"
That's it, that's all it was. Now, it has a bit more polishing to it, there is a main menu, which I thought of after seeing some of the projects in the Final Projects Gallery, and actually has some of the main poker rules built in it.
Of course, the program assumes that you KNOW how to play poker, and just need a money tracking program.
In hindsight, my project might sound pretty straightforward and easy to do, but it was actually pretty complex for someone like me to make it. In the end now, I have completed it to the best of my abilities.

So, once you start the program, there will be a basic menu on what you want to do. That's my main() function. You could choose how to use the program, see command help, launch the PokerTracker™ or exit.
The main meat of the program, is the poker() function. It handles everything basically. You'll be first prompted how many players, then name of each player and their starting balance, and the small blind(taken care of by the blind_bets() function). The player setup is maintained by the hence named player_setup() function
You'll be then prompted to either bet/raise/call, fold, check, declare somebody the winner, check someone's balance or see who all are left.
Checking someone's balance or seeing who is left won't consume your turn.
bet/raise/call are all one option, since it would have been too much effort for something so small. I'll implement it later on when I have free time. But, here is where you will need to know how to play poker. After picking bet/raise/call, you can enter a number which is bigger than or equal to the big blind, and smaller than or equal to your balance, or put in "small blind" or "big blind". As soon as the round starts, the first person has to put in small blind, and the second person has to put in big blind. That's the poker rules. Then, if someone raises, you have to put in enough money so that the amount you have contributed to the pot and the amount he has contributed to the pot is the same. This is something you'll need to be mindful of. Betting is taken care of by the bet_money() function.
Of course, if all but one person folds, the remaining person wins. This is overseen by the fold_check() function. Folding changes your class attribute of self.active to False, which is turned back to True when the next round starts, unless you don't have enough money.
The winning of the pot is taken care of by the pot_win() function.
If, let's say, due to some unforseen circumstances, you are out of money...
Worry not, I have thought about this. After a round is over, you will be prompted that *player* has not been added due to insufficient balance, and you'll be given a chance to input more money. This changes your self.active attribute back to True which allows you to participate in the rounds again.
Each round, the starting player is shifted to the player who went second the previous round.(akin to actual poker) This ensures that everyone will be small blind and big blind. When only one person has money left and everyone else has refused to add money, the person is announced as the winner and then the program exits.
I thought about adding save states, meaning if all the players have to stop for some reason, you could save the balances, and play again next time, but I thought that wasn't ~~true to the gambler's spirit~~ how actual games are ever played. 99% of times, people play until the others can't put any money in.
