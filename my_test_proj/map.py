import numpy

def inc(x):
    return x + 1
def searchbar():
    searchvalue = input("Search:\n")
    #print(f'Results for {value}')
    return searchvalue;

class Biz:
  def __init__(self, name, location, description):
    self.name = name
    self.location = location
    self.description = description

p1 = Biz("Westside", "Morningside Heights", "Grocery store")
p2 = Biz("Up", "Morningside Heights", "Coffee shop")

#Make a multidimensional list to store shops/businesses? a nested array?
Ls = [p1,p2]

