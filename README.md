# Counting Game

A fun number-ordering challenge built with Python and guizero. Click numbers in order as quickly as you can—track your score and race the clock!

## How to Run

1. Make sure Python is installed: https://python.org
2. Install the required library:
   
```bash
pip install guizero
```

3. Run the game (make sure all files are in one folder)

```
python gui.py
```
## How to Play
1. Enter your name in the text box.
2. Choose a difficulty level: Easy, Medium, Hard, or Extreme.
3. Click the "Press Start" button.
4. Click the numbers in the correct order (1, 2, 3...) as fast as possible.
5. A timer will start automatically.
6. If you click a number out of order, you’ll get an “Incorrect...” message.
7. Once you click all numbers correctly, you’ll see “You Win!” and your time will be saved.
8. Click Quit to close the game or try again by restarting.

## Demo!

Demonstrating the "Easy" level — other difficulties follow the same gameplay with more numbers and larger grids.

[View Demo Video Here](https://drive.google.com/file/d/1tR2p5boqh5GrsH1IOT9ZC05DLj43F6j2/view?usp=sharing)
   
## Files Description

- `gui.py` – GUI game using guizero
- `counting_game.py` – Game logic and score saving
- `title1.png` and `start3.png` – GUI image assets

## High Scores

The game creates `.txt` files to store your best times per difficulty level.

