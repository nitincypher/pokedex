
import os
import logging

def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n]

if __name__ == "__main__": 

    ## Make initial folder directories
    if(os.path.exists('./tmp') == False):
        os.mkdir('./tmp')

    ## Make PokeBatches
    n = 5
    text_file = open("./list.txt", "r")
    lines = text_file.readlines()
    x = list(divide_chunks(lines, n))
    index = 0 
    for pokebatch in x:
        with open('./tmp/pokebatch'+str(index)+'.txt', 'w+') as f:
            for pokemon in pokebatch:
                f.write("%s\n" % pokemon.strip())
        index = index + 1
    
    ## Run BingImageDownloader for each Pokebatch
    try:
        for i in range(0, index-1):
            os.system("python image_download.py -f ./tmp/pokebatch" + str(i) + ".txt --limit 50")
    except:
        print('Some Exception')
    finally:
        os.remove('./tmp')
    print("Done!") 