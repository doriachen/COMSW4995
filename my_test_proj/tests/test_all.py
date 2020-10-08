#import the method from project folder
from my_test_proj import inc
from my_test_proj import searchbar


#define test method for inc
def test_inc():
    assert inc(1) == 2, "did not pass test_inc"
    
#test 1 - takes in a string from searchbar
def test_searchbar():
    searchedvalue = isinstance(searchbar(), str)
    if searchedvalue:
        print("Pass test 1")
    else
        print("Fail test 1")

#test 2 - check if duplicates in list
def anydup(thelist):
  seen = set()
  for x in thelist:
    if x in seen: print("Fail test 2")
    seen.add(x)
  return print("Pass test 2")
    

#test 3 - check if a list item has missing info from specific fields


#test 4 - check if list is empty
def emptyList(thelist):
    if not a:
        print("Fail test 3)

#test 5 - 
