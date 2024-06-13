# Introduction

**Rock Paper Scissors** is a simple but classic hand game.
Each player simultaneously moulds one of three shapes with their hand: rock, paper or scissors. 
The rules of the game are very simple: the rock crushes the scissors, the scissors cut the paper and the paper covers the rock.

## Description
The code is written in Python (OOP). A Player class is the base from which different players can be selected when the game is running. Each player has their own strategy for making a move.

These are: 
- **Player** - always plays "Rock"
- **HumanPlayer** - asks for input from the user
- **RandomPlayer** - returns a random move
- **CyclePlayer** - plays cyclically from rock to paper and then to scissors

To change the player mode, go to dunder main.

The user can choose how many rounds he wants to play the game. 
