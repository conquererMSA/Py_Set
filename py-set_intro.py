'''
Set in python: Set is a unorderd collective data type that can hold any type of unique
value in curley braces.
in python set:
set are mutable and iterable.
set can accept any kind of immutable iterable data.
set can't accept mutable iterable as argument.
set unorderd collection tai indexing and slicing kora zay na.
we can create a set by 2 ways:
1. namesSet=set(iterable)
2. namesSet={'msa','pvs','mhd','thd'}
'''
names=['MSA','PVS','SMD','ALD','AHD','ABD']
namesSet=set(names)
# print(namesSet)
complexSet={'msa','MSA',2j+5,'3k+5',10,45.33,True,}
# print(type(complexSet)) # <class 'set'>
# print(complexSet)
complexSet.add('PVS')
# set er add method kuno kichu return kore na.
# print(complexSet)

#set er update method er maddhome oneg gulu item set e eksathe add kora zay
updatedSet=namesSet.update(['mfg','tty'])
# print(updatedSet) # None

# remove and delation item and whole set:
# set er moddye immutable data store korte hoy.
'''
set_name.discard(item) method exist item ke set theke remove kore, zodi kuno 
item set e exist na kore tahole discard diye remove korle error through kore 
na. discard method kuno kichu return kore na.

set_name.remove(item) method discard method er motoi item set theke remove kore , 
tobe item exist na korle keyError through kore.

set_name.pop() method randomly set theke kuno item remove kore dey. pop() method er 
kuno argument ney na. Tobe remove kora item return kore.

set_name.clear() method ekti set er sob item remove kore dey.  set empty kore dey.

'''
newSet={45.56,2j+7,'5k+6','Pvs','Mhd',(23,34,'MSA')}
# newSet.discard(2j+7) not error
# newSet.remove('salary') keyError karon salary item set e nei
# newSet.remove('Mhd') # remove 'Mhd' item from set
# removedItem=newSet.pop() #remove random item from newSet
# print(removedItem)
# newSet.clear()

#mathematical operation of set
setA={1,2,3,4,5,6,1,3}
subOfA={3,6,1,4}

setB={4,5,6,7,8,9,3}
subOfB={4,5,8,9}
'''
union: duti set er sobgulu item niye notun set toire kore.

intersection: duti set er moddhyekar common item niye notun set toire kore

diffrence: duti set er moddhykar common item gulu bad diye and proto set er baki item 
gulu niye new set toire kore.

symmetric_difference/setA^setB: duti set er moddhykar uique item gulu niye symmetric 
diffrence set toire hoy.

set_name.copy(): ekti set er item gulu niye arekta set toire kore.


'''
unionAB=setA.union(setB) # setA|setB
insecAB=setA.intersection(setB) #setA & setB
# insecBA=setB.intersection(setA)
# print(insecBA)
aDiffb=setA-setB
bDiffa=setB-setA
# print(aDiffb)
# print(bDiffa)
symDiffAB=setA^setB
symDiffAB2=setA.symmetric_difference(setB)
# print(symDiffAB,symDiffAB2)

# print(subOfA.issubset(setA)) #True
# print(setA.issuperset(subOfA)) #True

setA2=setA.copy()
# print(setA2)

#modify sets based on their relationship with other sets.
'''
difference_update() removes the elements that are present in the second set from the first set.

intersection_update() updates the first set with the elements that are present in both the first and second sets.

symmetric_difference_update() updates the first set with the elements that 
are present in either the first or second set, but not in both

isdisjoint() returns True if the two sets have no elements in common, False otherwise.
'''
pp=setA.difference_update(setB)
# print(pp)
pp2=setA.intersection_update()
# print(pp2)
pp3=setB.symmetric_difference_update(setA)
pp4=setB.isdisjoint(setA)
print(pp4)