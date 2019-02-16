import threading 
import Pokemon
import scraper

def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n]

if __name__ == "__main__": 
    n = 5
   
    # creating thread 
    
    x = list(divide_chunks(Pokemon.getPokemonNames(), n)) 
    for pokebatch in x:

        tlist = []

        for pokemon in pokebatch:
            tlist.append(threading.Thread(target=scraper.run, args=(pokemon,)))
  
        # starting threads
        for thd in tlist:
            thd.start()
  
        for thd in tlist:
            thd.join()
  
    # both threads completely executed 
    print("Done!") 