
#Create a function that enter a list of number, and returns all the numbers in one
 # in one string seperated by '/'
# res="1/2/3/4/5/6"


def convert_number_to_str(arr):
    new_arr=[]
    for i in arr:
        new_arr.append(str(i))
    return new_arr

# #join function python
# print(convert_number_to_str([1,3,5,7]))


def join_number(n,sep):
    new_arr=[]
    for i in range (1,n+1):
        new_arr.append(str(i))
    new_arr=sep.join(new_arr)
    return new_arr

# print(join_number(7,' '))


#Take a list, any list, make a function that returns everything in the list but squared

def to_square(arr):
    new_arr=[]
    for i in arr:
        new_arr.append(i*i)
    return new_arr

# print(to_square([5,1,2,7]))


#You'll have a list like this, [1,2,8,9,0,34],
#  i want to create a function that puts all the even number in the beginning of the list, and all the
#odds at the end

#even -> pair
#odd -> impair

def segregation_hugo(arr):
    return list([i for i in arr if not(i%2)]+[i for i in arr if i%2])

# print(segregation_hugo([1,6,7,87,5,4,6,90,43,3,12,16,29]))


# #Create new list
# if i in list is even add to new list
# once it's done
# do the same for odd numbers and always add at the -end- of the list
# then you'll have the final answer'


def segregation(arr):
    new_arr=[]
    for i in arr:
        if i%2 == 0:
            new_arr.append(i)
    for i in arr:
        if i%2 != 0:
            new_arr.append(i)
    return new_arr

# print(segregation([1,2,3,4,5]))

keys='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def replace(thingy,keys):
    new_str=''
    for i in keys:
        if i == thingy:
            new_str+='#'
        else:    
            new_str+=i
    return new_str

# print(replace("K", keys))


#Create a function that has an input keys and word. Replace all the letters of the word inside keys by '#'
#Ex: print(replace_all_word(keys,'HUGO'))
#-> ABCDEF##IJKLMN#PQRST#VWXYZ

def replace_all_word(keys,word):
    new_str=''
    for i in keys:
        if i in word:
            new_str+='#'
        else:
            new_str+=i
    return new_str

# print(replace_all_word(keys, "HUGO"))
#Create a function that takes a list of any numbers and that returns all numbers 
# divisible at the start of the list
#Ex: print(sort_divisible_by_3(arr)), arr=[1,4,9,81,56,91,90,57]
#->'9 81 90 57 1 4 56 91'

arr=[1,4,9,81,56,91,90,57]

def sort_divisible_by_3(arr):
    new_arr=[]
    str_arr=[]
    sep=' '
    for i in arr:
        if i%3 == 0:
            new_arr.append(i)
    for i in arr:
        if i%3 != 0:
            new_arr.append(i)
    for i in new_arr:
        str_arr.append(str(i))
    str_arr=sep.join(str_arr)
    return str_arr

# print(sort_divisible_by_3(arr))


# Make a function that counts the occurence of a letter inside a text
# print(count_occurences('Hm Watcha sayyyy , oh that you on did welll, or cause you did, oh whatcha say', 'a'))
#-> 8

#The program should able to also count capital As

def count_occurences(text, letter):
    count=0
    for i in text:
        if i == letter.upper() or i == letter:
            count += 1
            print(i)
    return count

# print(count_occurences('Hm Watcha sayyyy ,AAAAAAAAAAAA oh that you on did welll, or cause you did, oh whatcha say', 'a'))


#Create a function that counts the numbers of voyels inside the sentence.

def count_voyels(sentence):
    voyels='aeiouy'
    count=0
    for i in sentence:
        if i in voyels:
            count+=1
    return count

# def count_voyels(sentence):
#     return len([i for i in sentence if i in 'aeiouy'])

# print(count_voyels('Hm Watcha sayyyy ,AAAAAAAAAAAA oh that you on did welll, or cause you did, oh whatcha say'))





#-----------------------------------------------------------------------------------------------------------------

#Create a whole program that asks an input from the user, and with the input, replace the word in the alphabet
#The program will look like this

#-> Please enter a letter:
#-> A
#->#BCDEFG...
#-> Please enter a letter:
#-> E
#-> #BCD#FG.....

#The program stops and says 'Bruh' when all the voyels has been cleared out
#Check the 'Replace' function 



def main():
    voyels='aeiouy'
    display='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter=input('Please enter a letter: ')
    for i in display:
        if i == letter:
            new_display = display.replace(letter, "#")
            print(display)
            print(new_display)


def main():
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    voyels='AEIOUY'
    stock=''
    while stock!=voyels:
        letter=input('Please enter a letter:').upper()
        if letter in voyels:
            stock+=letter
            stock=''.join(sorted(stock))
        alphabet=alphabet.replace(letter, "#")
        print(alphabet)
        print(stock)
    print('Bruh')
            
# main()
        
#CrEaTe mE a FuNcTiOn tHaT TaKeS a SeNteNcE aNd TrAnSfoRms iT lIkE tHiS

def upper_luck(text):
    count=0
    for letter in text:
        if count%2 == 0:
            text=text.replace(letter, letter.upper())
        count+=1
    return text

def upper_luck2(text):
    new_arr=list(text)
    new_str=''
    for i in range(len(text)):
        if i%2==0:
            new_str+=new_arr[i].upper()
        else:
            new_str+=new_arr[i]
    return new_str

# print(upper_luck2('zertyuiopjhgfdsxcvbhjk

#Create a fibibonacci sequence until an N found and get the sum of the list at the Nth element



def opposite_number(string):
    return eval(string)*-1

# print(opposite_number('-1.25'))

txt = 'Hm Watcha sayyyy oh that you on did welll or cause you did oh whatcha say'

def long_word(txt):
    txt_split = txt.split(" ")
    txt_list = []
    for i in txt_split:
        txt_list.append(len(i))
        print('txt_list = ',txt_list)
    return max(txt_list)

# print(long_word(txt))



# ------------------------------------------------------------------------------------------------------------



#Make the following functions
#---------------------------
#1) Check if the username is already in the list
#2) If it is, return the index of the username
#3) Add a username to the list to a random place and in the end print something like 'Bruh:8' ('username':index)

#1) def check_username(username,usernames):
#2) def get_username_index(username,usernames):
#3) def add_username(username,usernames):

#---------------------------
#4) Sort the list of usernames in alphabetical order
#5) Sort the list of usernames in reverse alphabetical order
#6) Sort the list of usernames by length of the username

#4) def sort_usernames(usernames):
#5) def sort_usernames_reverse(usernames):
#6) def sort_usernames_length(usernames):

#---------------------------
#7) Sort the list of usernames by the number of vowels in the username
#8) Sort the list of usernames by the number of consonants in the username

#7) def sort_usernames_vowels(usernames):
#8) def sort_usernames_consonants(usernames):

#-------------------------------------------------------------------------------------------------------------

usernames=['Hugo','Leo','Léo','Léa','Tom','Téo','Téa','Lola']

def check_username(username,usernames):
    for i in usernames:
        if i == username:
            return True
    return False

# def check_username(username,usernames):
#     if username in usernames:
#         return True
#     return False
    
# def check_username(username,usernames):
#     return username in usernames

def get_username_index(username,usernames):
    count=0
    for i in usernames:
        if i == username:
            return count
        count+=1
    return False

# def get_username_index(username,usernames):
#     return usernames.index(username)

# print(get_username_index('Léa',usernames))

import random
def random_choice(usernames):
    return random.randint(0, len(usernames))

def add_username(username,usernames):
    if username in usernames:
        return f'{username} : {usernames.index(username)} (was in list)'
    index = random_choice(usernames)
    usernames.insert(index,username)
    return f'{username} : {index}'
# print(add_username('Hugo', usernames))
# print(add_username())
# cree un liste
# genere un nombre entre a et b
# ajouter un element a un index dans une liste

def alpha_sort(usernames):
    return sorted(usernames)

# print(goulou(usernames))

def reversed_alpha_sort(usernames):
    return list(reversed(sorted(usernames)))

# print(reversed_alpha_sort(usernames))

def sort_usernames_length(arr):
    new_arr = []
    for index in range(1,max([len(i) for i in arr])+1):
        for names in arr:
            if index == len(names):
                new_arr.append(names)
    return new_arr

# print(sort_usernames_length(usernames))


#-------------------------------------------------------------------------------

simple_str= "123456759"
#1)Do a function to convert the string to a list
#-> ['1','2','3','4','5','6','7','5','9']
arr_1=[1,2,3,4,5,6,7,5,9]
#2)Do a function that sorts even numbers first and odd numbers last
#-> [2,4,6,8,1,3,5,7,9]
arr_of_words=['car','house','cat','dog','apple','banana','orange','pear']
#3)Do a function that counts each voyels in each word in a new array
#-> ['car','house','cat','dog','apple','banana','orange','pear']
#-> [1,2,0,1,2,3,3,1]

#-------------------------------------------------------------------------------


def convert_str(simple_str):
    new_arr=[]
    for i in simple_str:
        new_arr.append(i)
    return new_arr

# print(convert_str(simple_str))


def even_number(arr_1):
    new_arr = []
    for i in arr_1:
        if i%2 == 0:
            new_arr.append(i)
    for i in arr_1:
        if i%2 != 0:
            new_arr.append(i)
    return new_arr

# print(even_number(arr_1))


def number_voyels(arr_of_words):
    voyels_str='aeiouy'
    new_arr=[]
    count=0
    for word in arr_of_words:
        for letter in word:
            if letter in voyels_str:
                count+=1
        new_arr.append(count)
        count=0
    return new_arr

# print(number_voyels(arr_of_words))

#-----------------------------------------------------

#1) Given any arr, find the maximum integer in the array and return it
#2) Given any arr, find the minimum integer in the array and return it
#3) Given an arr, find the highest occurences of consecutive integers and return it
#4) Given an arr, find the lowest occurences of consecutive integers and return it

#1) def find_max(arr):
#2) def find_min(arr):
#3) def find_max_consecutive(arr):
#-> [1,1,1,1,2,2,2,4,6,7,8,3,1,6]
#-> 5
#4) def find_min_consecutive(arr):
#-> [1,1,1,1,2,2,2,4,4,6,7,8,8,3,3,1,6,6]
#-> 1

#------------------------------------------------------
example_arr=[1,1,1,1,2,2,2,4,6,7,8,3,1,6]

def find_max(arr):
    return max(arr)

# print(find_max(example_arr))


def find_min(arr):
    return min(arr)

# print(find_min(example_arr))


def find_max_occurences(arr):
    arr=list(sorted(arr))
    single_arr=[]
    occurences=[]
    count=0
    for i in list(sorted(arr)):
        if i not in single_arr:
            single_arr.append(i)
    for j in single_arr:
        for i in arr:
            if i == j:
                count+=1
        occurences.append(count)
        count=0
    index=max(occurences)
    return index

# print(find_max_occurences(example_arr))

def find_min_occurences(arr):
    arr=list(sorted(arr))
    single_arr=[]
    occurences=[]
    count=0
    for i in list(sorted(arr)):
        if i not in single_arr:
            single_arr.append(i)
    for j in single_arr:
        for i in arr:
            if i == j:
                count+=1
        occurences.append(count)
        count=0
    index=min(occurences)
    return index

# print(find_min_occurences(example_arr))

binaire1='1001'
binaire2='1010'
binaire3='1100'
binaire4='1101'
binaire5='1110'
binaire6='1111'

#Convert those binary numbers to decimal using a function


def binaire_to_decimal(string):
    a,b,c,d=int(string[0]),int(string[1]),int(string[2]),int(string[3])
    return a*(2**3)+b*(2**2)+c*(2**1)+d*(2**0)

def binaire_to_decimal(string):
    return int(string,2)

# print(binaire_to_decimal(binaire1))


#Create a function that takes in 3 parameters: start, to, n
#from: will be the initial number
#to: the limiter number
#n: the len of the array that is supposed to be generated
#Ex: def number_generator(from,to,n):
#-> def number_generator(1,130,20):
#-> output: [3,4,76,ect...]
#The function will have to generate an array of len 'n' and have random generated number from 'from' to 'to'

#random_arr=[4,7,9,8,92,39,32,87,9,34,12,86,112,23]
#Without using '%' create a function that checks whethers the numbers are divisible by '3'
#You should return an arr like [True,False,True,True,ect...]

import random
def number_generator(start,to,n):
    finish_arr=[]
    for i in range(n):
        finish_arr.append(random.randint(start, to))
    return finish_arr

# print(number_generator(0,100,20))

def divisible_3(arr):
    result_arr=[]
    for i in arr:
        if (i/3 - int(i/3)) == 0.0:
            result_arr.append('True')
        else:
            result_arr.append('False')
    return result_arr

# print(divisible_3(number_generator(0,100,20)))



print("cerise")