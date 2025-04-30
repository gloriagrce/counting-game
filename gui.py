"""
A GUI controller for a Counting game.

Since Project 3, I have added the randomize number features, timer, and memory to store the name and time.
Since Project 4, I have added the high score feature and a quit button.

@author: Gloria Grace (gg33)
@date: Fall, 2021
"""

from guizero import App, Text, PushButton, Box, Picture, TextBox, ButtonGroup
from datetime import datetime
from Counting_game import Counting


class CountingApp:
    
    def __init__(self, app):
        """ Constructor that edit the app and draws the widgets of introduction to the user."""
        
        # Configure the application GUI.
        app.title = 'Counting Game'
        app.font = 'Nexa Bold'
        app.text_size = 12
        app.height = 550
        
        # set default grid for level difficulty
        self.cell_width = 5
        self.cell_height = 2
        
        # Instantiates the counting game.
        self.counting = Counting()
        
        # Add the operand-input widgets.
        self.start_box = Box(app, layout='grid')
        Picture(self.start_box, image='title1.png', grid=[0, 3], width=400, height=200)
        Text(self.start_box, text="Enter your name:", grid=[0, 4], align="left")
        self.user_input = TextBox(self.start_box, width=14, grid=[0, 4], align="right")
        Text(self.start_box, text="          ", grid=[0, 7])
        PushButton(self.start_box, text='high score', grid=[0, 10], command=self.get_high_score, align='left')
        self.hs = TextBox(self.start_box, width=14, grid=[0, 10], align='right')
        
        # Select Level
        self.level_choice = ButtonGroup(self.start_box, options=['Easy', 'Medium', 'Hard', 'Extreme'], grid=[0, 8], align="left", command=self.level_difficulty)
        
        # Start Button Widget
        PushButton(self.start_box, image='start3.png', grid=[0, 8], align="right", width=200, height=175, command=self.start_game)
        
        # Game box
        self.game_box = Box(app, layout='grid')
        
        self.buttons = []
        self.level_limit = ''
    
    def start_game(self):
        """ This method start and open the game when the button is pushed."""
        
        
        # Game Box Layout for each levels.
        app.width = self.cell_width * 155
        
        if self.level_choice.value == 'Easy':
            app.height = self.cell_width * 100
            
        else:
            app.height = self.cell_width * 165
        
        # Get the randomize number list.
        numbers = self.counting.get_random_numbers(self.level_choice.value)
        
        k = 0
        
        # Loop that makes the buttons and assign text in them.
        for i in range(self.cell_width):
            for j in range(self.cell_height):
                self.button = PushButton(self.game_box, width=3, height=1, grid=[i,j], text=numbers[k], command=self.operation, args=[k])
                self.button.text_size = 35
                self.buttons.append(self.button)
                k += 1
        
        # Text if user made a mistake or won.
        Text(self.game_box, text="          ", grid=[0, 8])
        self.check = Text(self.game_box, grid=[self.cell_width // 2, 10])
        Text(self.game_box, text="          ", grid=[0, 11])
        
        # Set up the timer.
        self.timer = Timer()
        self.text = Text(self.game_box, grid=[self.cell_width // 2, 11])
        
        # Start the counter.
        self.update_clock()
        app.repeat(10, self.update_clock)
        
        # Quit button.
        PushButton(self.game_box, text='Quit', grid=[0, 10], align='right', command=app.destroy)
                
        # Hide the Menu and opens the game.      
        self.game_box.hide()
        self.start_box.hide()
        self.game_box.show()
       

    def level_difficulty(self):
        """ This method change the grid setup based on the level that the user chooses."""
        
        if self.level_choice.value == 'Easy':
            self.cell_width = 5
            self.cell_height = 2
            
        elif self.level_choice.value == 'Medium':
            self.cell_width = 5
            self.cell_height = 4
           
        elif self.level_choice.value == 'Hard':
            self.cell_width = 5
            self.cell_height = 5
            
        elif self.level_choice.value == 'Extreme':
            self.cell_width = 6
            self.cell_height = 6
        
    def operation(self, position):
        """ Conditions if the user made the correct push button or not which can lead to winning."""
        
        # Set limit of the numbers based on the levels.
        if self.level_choice.value == 'Easy':
            self.level_limit = '10'
            
        elif self.level_choice.value == 'Medium':
            self.level_limit = '20'
           
        elif self.level_choice.value == 'Hard':
            self.level_limit = '25'
            
        elif self.level_choice.value == 'Extreme':
            self.level_limit = '36'
        
        check = self.counting.calculation_check(self.buttons[position].text)
        
        # Statement if the calculation is correct.
        if check == True:
            
            # Check if the last button is pressed, it means the user won.
            if self.buttons[position].text == self.level_limit:
                self.buttons[position].text = ''
                self.buttons[position].enabled = False
                self.check.value = 'You Win!'
                self.store_score()
            
            # Every other buttons.
            else:
                self.buttons[position].text = ''
                self.buttons[position].enabled = False
                self.check.value = ''
        
        # Statement if the user pressed a button in the incorrect order.
        elif check == False:
            self.check.value = 'Incorrect...'
            
    def update_clock(self):
        """ Update the value of the timer to the GUI."""
        
        # Stop the timer if user win.
        if self.check.value == 'You Win!':
            return self.text.value
            
        else:
            self.text.value = '{:.02f}'.format(self.timer.get_time())
              
    def store_score(self):
        """ Call the method in the game program to make a list full of scores."""
        
        self.counting.set_score(self.user_input.value, self.text.value, self.level_choice.value)
    
    def get_high_score(self):
        """ Get the highest score from the score list."""
        
        self.hs.value = self.counting.high_score(self.level_choice.value)
        
class Timer:
    
    def __init__(self):
        """ Resets everytime the app is called."""
        
        self.reset()

    def reset(self):
        """ Reset method that get the timer back from the start."""
        
        self.start_time = datetime.now()

    def get_time(self):
        time_since_start = datetime.now() - self.start_time
        return time_since_start.total_seconds()

        
app = App()
CountingApp(app)
app.display()
