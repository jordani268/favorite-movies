favmovlist = []
print("What are your 4 favorite movies")
num = 1

while len(favmovlist) < 5:
    favmovadd = input(f"What is your number {num} favorite movie? ")
    favmovlist.append(favmovadd)
    num += 1 
    if len(favmovlist) == 4:
        break
        
print(f"Your favorite movies are {favmovlist[0]}, {favmovlist[1]}, {favmovlist[2]}, and {favmovlist[3]}.")
