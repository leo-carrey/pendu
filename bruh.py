
#Create a function that enter a list of number, and returns all the numbers in one
 # in one string seperated by '/'
# res="1/2/3/4/5/6"

# def join_number_with_slash(arr):

#     return arr


# def convert_number_to_str(arr):
#     new_arr=[]
#     for i in arr:
#         new_arr.append(str(i))
#     return new_arr

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

print(segregation([1,2,3,4,5]))