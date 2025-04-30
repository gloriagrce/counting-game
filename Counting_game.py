"""
The Counting Game Application.

From project three, I have added the get random numbers method, the board state,
the calculation for the game, and set name and timer, and a list for all the players score (high score).

@author: Gloria Grace (gg33)
@date: Fall, 2021
"""
import random

class Counting:
    
    def __init__(self):
        """ Creates self constructors."""
        
        self.number_list = []
        self.count = 0
        self.name = ''
        
    def __str__(self):
        """ Returns the board state easy mode. """
        
        return '1 | 2 | 3 | 4 | 5\n' + '-' * 20 + '\n' + '6 | 7 | 8 | 9 | 10'
        
    def get_random_numbers(self, level):
        """ Put randomize numbers on a list depending on the level of it."""
        
        if level == 'Easy':
            for i in range(1, 11):
                self.number_list.append(i)
                random.shuffle(self.number_list)
            
        elif level == 'Medium':
            for i in range(1, 21):
                self.number_list.append(i)
                random.shuffle(self.number_list)
           
        elif level == 'Hard':
            for i in range(1, 26):
                self.number_list.append(i)
                random.shuffle(self.number_list)
            
        elif level == 'Extreme':
            for i in range(1, 37):
                self.number_list.append(i)
                random.shuffle(self.number_list)
        
        return self.number_list
    
    def calculation_check(self, value):
        """ Determine if the user did the right calculation or counting."""
        
        if int(value) - self.count == 1:
            self.count += 1
            return True
        
        else:
            return False
            
    def set_score(self, name, time, level):
        """ Store the name, time, and level into memory."""
        
        self.name = name
        self.time = time
        self.level = level
        
        self.score_board()
 
    def score_board(self):
        """Store different list of scores based on the levels."""
        
        # Make a new file that lists the scores and names.
        if self.level == 'Easy':
            score = open('easy-scores.txt', 'a')
            
        elif self.level == 'Medium':
            score = open('medium-scores.txt', 'a')
        
        elif self.level == 'Hard':
            score = open('hard-scores.txt', 'a')
            
        elif self.level == 'Extreme':
            score = open('extreme-scores.txt', 'a')
        
        score.write(self.name + ',' + self.time + '\n')
        score.close()
    
    def high_score(self, level):
        """ Method that open the score file and find the fastest score out of all."""
        
        score_list = []
        
        # Read the level based score files.
        if level == 'Easy':
            score = open('easy-scores.txt')
            
        elif level == 'Medium':
            score = open('medium-scores.txt')
        
        elif level == 'Hard':
            score = open('hard-scores.txt')
            
        elif level == 'Extreme':
            score = open('extreme-scores.txt')

        # Split the format to variables.
        for line in score:
            values = line.split(',')
            
            scores = Scores(values[0], values[1])
            score_list.append(scores)
        
        # Default the fastest score to the first player.
        fast_score = score_list[0]
        
        # From the list, find the fastest score out of all the players that had played.
        for scores in score_list:
            if fast_score.time > scores.time:
                fast_score = scores
         
        # Write and create a new file only to store the fastest score.
        if level == 'Easy':
            hs = open('easy-hs.txt', 'w')
            
        elif level == 'Medium':
            hs = open('medium-hs.txt', 'w')
        
        elif level == 'Hard':
            hs = open('hard-hs.txt', 'w')
            
        elif level == 'Extreme':
            hs = open('extreme-hs.txt', 'w')
        
        hs.write(str(fast_score))
            
        hs.close()
    
        return fast_score
        
        
class Scores:

    def __init__(self, given_name='John Doe', time=0):
        """Instantiate a new score object, defaulting to a basic John Doe."""
        
        self.given_name = given_name
        self.time = time
        
    def __str__(self):
        """ Create a score string with a simple format."""
        
        return self.given_name + ' :  ' + self.time + ' s'