import json
import os
import string
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")

class LetterFrequency:
    letters = list(string.ascii_uppercase)
    frequency = dict()
    percentage = dict()
    total_letters = 0

    def __init__(self, path="books", img="fig.png"):
        self.path = path
        self.img = img 
        self.files = os.listdir(path)
        for letter in self.letters:
            self.frequency[letter] = 0

    def count_letters(self):
        for fname in self.files:
            print("READING:", fname)
            with open(os.path.join(self.path, fname), encoding="utf-8") as f:
                text = f.read()
                for letter in text:
                    letter = letter.upper()
                    if not letter in self.letters:
                        continue

                    self.frequency[letter] += 1
        
        self.total_letters = sum(self.frequency.values())

    def calculate_percentage(self):
        self.percentage = self.frequency.copy()

        for letter in self.percentage:
            self.percentage[letter] = round(self.percentage[letter]*100/self.total_letters, 3)
        
        print(self.percentage)

    def plot(self):
        plt.bar(self.percentage.keys(), self.percentage.values())
        plt.title("English Letters Frequency")
        plt.xlabel("Letters")
        plt.ylabel("Percentage")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(self.img)
        plt.show()