import os

def Diff(li1, li2): 
    return (list(set(li1) - set(li2))) 

folders = []
names = []
os.remove('./listnew.txt')
for dir in os.listdir('./images'):
    folders.append(dir)

text_file = open("./list.txt", "r")
lines = text_file.readlines()
for words in lines:
    names.append(words.strip())

print(Diff(names, folders))

with open('./listnew.txt', 'w+') as f:
    for pokemon in Diff(names, folders):
        f.write("%s\n" % pokemon.strip())


