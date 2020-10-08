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
        print("fail test 1")

#test 2 - 


#test 3 -


#test 4 - 


#test 5 - 
