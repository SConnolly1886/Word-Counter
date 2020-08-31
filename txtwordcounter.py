"""
Write a program that reads the words in words.txt and stores
them as keys in a dictionary. It doesn't matter what the values are.
Then you can use the in operator as a fast way to check whether a
string is in the dictionary.
"""
fname = input('Enter file name: ')
if len(fname) < 1 : fhandle = open('romeo.txt')
else:
    try:
        fhandle = open(fname)
    except:
        print('Invalid input')
        quit()
wordslist = {}
for lines in fhandle :
    lines = lines.rstrip()
    words = lines.split()
    for word in words:
            wordslist[word] = wordslist.get(word, 0) + 1

keylist = list(wordslist.keys())
print(keylist)
keylist.sort()
for key in keylist :
    print(key, wordslist[key])
#print(wordslist)
