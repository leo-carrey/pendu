dico_plantes={
    'arbre':{
        'chêne':500,
        'baobab':3000,
        'néfliers':200,
    },
    'fleurs':{
        'rose':50
    }
}

petit_dico_arbre=dico_plantes['arbre']

# print(petit_dico_arbre['néfliers'])


arr_5=[1,2,3,4,5]

def add_n(arr,n):
    new_arr=[]
    for i in arr:
        new_arr.append(i+n)
    return new_arr

import random
def number_generator(start,to,n):
    finish_arr=[]
    for i in range(n):
        finish_arr.append(random.randint(start, to))
    return finish_arr

# print(add_n(arr_5,50))



def to_uppercase(arr):
    new_arr=[]
    for i in arr:
        new_arr.append(i.upper())
    return new_arr

# print(to_uppercase(['hugo','leo','livio']))

def upper_start(arr):
    new_arr = []
    for i in arr:
        new_arr.append(i[0].upper()+i[1:])
    return new_arr


# print(upper_start(['hugo','leo','livio']))


def spot_the_difference(arr):
    common_term=''
    res=''
    for letter in arr[0]:
        if letter in arr[1]:
            common_term+=letter
    for word in arr:
        for letter_to_replace in common_term:
            word=word.replace(letter_to_replace,'')
        res+=word
    return res

# print(spot_the_difference(['burh','brah','borh','bryh','brkh','bjrhaaa']))


dioc_bruh={
    'bruh':50,
    'bro':25,
    'big':1000
}

dioc_bruh['brah']=69


def sum_odd(arr):
    new_arr=[]
    for number in arr:
        if number%2 != 0:
            new_arr.append(number)
    return sum(new_arr)


def sum_odd(arr):
    return sum([i for i in arr if i%2 != 0])


# print(sum_odd([1,3,5,4,6,8]))

#Create a function that has an input keys and word. Replace all the letters of the word inside keys by '#'
#Ex: print(replace_all_word(keys,'HUGO'))
#-> ABCDEF##IJKLMN#PQRST#VWXYZ

keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def replace_letters(keys,word):
    for letter in word:
        keys = keys.replace(letter,"#")
    return keys

# print(replace_letters(keys,"HUGO"))



def find_even(arr):
    count=0
    for i in arr:
        if len(i)%2==0:
            count+=1
    return count

# print(find_even(["jax","pierre","gwen","hugo"]))


# print(7**2)
import math
def nearest_square(number):
    low_value=int(math.sqrt(number))
    high_value=int(math.sqrt(number))+1
    if number-low_value**2>high_value**2-number:
        return high_value
    return low_value

print(f"bing chi{nearest_square(111)}ing, 冰淇淋")
