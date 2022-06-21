{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ccbc97b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rock, Paper, Scissors?Rock\n",
      "You win! Rock smashes Scissors\n",
      "Rock, Paper, Scissors?scissors\n",
      "That's not a valid play. Check your spelling!\n",
      "Rock, Paper, Scissors?Scissors\n",
      "You win! Scissors cut Paper\n",
      "Rock, Paper, Scissors?Rock\n",
      "You win! Rock smashes Scissors\n",
      "Rock, Paper, Scissors?Paper\n",
      "You lose! Scissors cut Paper\n"
     ]
    }
   ],
   "source": [
    "from random import randint\n",
    "\n",
    "#create a list of play options\n",
    "t = [\"Rock\", \"Paper\", \"Scissors\"]\n",
    "\n",
    "#assign a random play to the computer\n",
    "computer = t[randint(0,2)]\n",
    "\n",
    "#set player to False\n",
    "player = False\n",
    "\n",
    "while player == False:\n",
    "#set player to True\n",
    "    player = input(\"Rock, Paper, Scissors?\")\n",
    "    if player == computer:\n",
    "        print(\"Tie!\")\n",
    "    elif player == \"Rock\":\n",
    "        if computer == \"Paper\":\n",
    "            print(\"You lose!\", computer, \"covers\", player)\n",
    "        else:\n",
    "            print(\"You win!\", player, \"smashes\", computer)\n",
    "    elif player == \"Paper\":\n",
    "        if computer == \"Scissors\":\n",
    "            print(\"You lose!\", computer, \"cut\", player)\n",
    "        else:\n",
    "            print(\"You win!\", player, \"covers\", computer)\n",
    "    elif player == \"Scissors\":\n",
    "        if computer == \"Rock\":\n",
    "            print(\"You lose...\", computer, \"smashes\", player)\n",
    "        else:\n",
    "            print(\"You win!\", player, \"cut\", computer)\n",
    "    else:\n",
    "        print(\"That's not a valid play. Check your spelling!\")\n",
    "    #player was set to True, but we want it to be False so the loop continues\n",
    "    player = False\n",
    "    computer = t[randint(0,2)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f70e64af",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
