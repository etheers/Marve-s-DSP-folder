{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ded72e9f-2cb8-430a-882a-d7ccfe8df11c",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a word:  marve bicbic\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reversed Word (in all caps): CIBCIB EVRAM\n",
      "Word Length: 12\n"
     ]
    }
   ],
   "source": [
    "def reverse_string(word):\n",
    "    reversed_word = word[::-1]\n",
    "    reversed_word_caps = reversed_word.upper()\n",
    "    word_length = len(word)\n",
    "    return reversed_word_caps, word_length\n",
    "\n",
    "# Get input from the user\n",
    "input_word = input(\"Enter a word: \")\n",
    "\n",
    "# Call the function to reverse the word and get its length\n",
    "reversed_word, word_length = reverse_string(input_word)\n",
    "\n",
    "# Display the results\n",
    "print(f\"Reversed Word (in all caps): {reversed_word}\")\n",
    "print(f\"Word Length: {word_length}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8e8f60a7-7c4e-461f-8445-3cf6167a1993",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input:  Marve Bicbic\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Output: CIBCIB EVRAM\n",
      "Word Length: 12\n"
     ]
    }
   ],
   "source": [
    "def reverse_string(word):\n",
    "    reversed_word = word[::-1]\n",
    "    reversed_word_caps = reversed_word.upper()\n",
    "    word_length = len(word)\n",
    "    return reversed_word_caps, word_length\n",
    "\n",
    "# Get input from the user\n",
    "input_word = input(\"Input: \")\n",
    "\n",
    "# Call the function to reverse the word and get its length\n",
    "reversed_word, word_length = reverse_string(input_word)\n",
    "\n",
    "# The results\n",
    "print(f\"Output: {reversed_word}\")\n",
    "print(f\"Word Length: {word_length}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74f61ec9-79f6-4019-9e2e-43a76472b400",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
