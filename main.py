from charactes import*
from enemise import*

#enemies
grob = Gobline("Grob",10,30)
vlad = Vampire("Dracula",12,40)

#players
boris = fighter("Boris",15,50)
anna = Healer("Anna",7,35)

print("--- Stats before fight ---")
print(grob,vlad,boris,anna,sep="\n")

#Enemies turn
grob.attack(boris)
vlad.attack(boris)

#players turn
boris.attack(vlad)
anna.heal(boris)

#enemies turn
grob.attack(anna)
vlad.life_steal(anna)

print("---stats after fight---")
print(grob,vlad,boris,anna,sep="\n")