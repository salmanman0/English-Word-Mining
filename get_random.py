import random
import pandas as pd

x = pd.read_csv('unigram_freq.csv')
fruits = pd.read_csv('fruits.txt')
house = pd.read_csv('house.txt')
food = pd.read_csv('food_and_drink.txt')
general_word = list(x['word'])
sample_word = list(set(x['word'].unique()))
sample_fruit = list(set(fruits['fruit'].unique()))
sample_house = list(set(house['word'].unique()))
sample_food = list(set(food['word'].unique()))

def generate_word():
    if not sample_word:
        return None 
    random_word = random.choice(sample_word)
    sample_word.remove(random_word)
    return random_word

def not_random(index) :
    return general_word[index]

def generate_fruit():
    if not sample_fruit:
        return None 
    random_word = random.choice(sample_fruit)
    sample_fruit.remove(random_word)
    return random_word


def generate_house():
    if not sample_house:
        return None 
    random_word = random.choice(sample_house)
    sample_house.remove(random_word)
    return random_word

def generate_food():
    if not sample_food:
        return None 
    random_word = random.choice(sample_food)
    sample_food.remove(random_word)
    return random_word


# Tes penggunaan

# for i in range(5): 
#     word = not_random(i)
#     print(f"Kata acak yang unik: {word}")

print(not_random(5))