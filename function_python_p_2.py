#    -> max and min <-

#print(max(2,3))
#print(max([1,20,65,100,1000]))
#print(min([1,20,65,100,1000]))


#   -> enumerate <-

#for letter in ['a','b','c']:
#    print(letter)

#mylist = ['a','b','c']
#index = 0
#for letter in mylist:
#    print(letter)
#    print('is at index: {}'.format(index))
#    index = index+1
#    print('')

#mylist = ['a','b','c']
#for index,item in enumerate(mylist):
#    print(item)
#    print(f"is at index {index}")
#    print('')

#     -> .join <-

#mylist = ['a','b','c','d']

#print(''.join(mylist))
#print('--'.join(mylist))


#def secret_check(mystring):
#    if 'secret' in mystring:
#        return True
#    else:
#        return False
#print(secret_check('this is a secret'))


#def secret_check(mystring):
#    return 'secret' in mystring
#print(secret_check('this is a ')) 

#problem2
# create a code maker function. this function will take in a 
# string name and replace any vowels with the letter x.

def code_maker(mystring):
    
    output = list(mystring)
   
    for index,letter in enumerate(mystring):
        for vowel in 'aeiou':
            if letter.lower() ==vowel:
              output[index] = 'x'
    output = ''.join(output)
    return output
    
print(code_maker('Adam')) 
    



