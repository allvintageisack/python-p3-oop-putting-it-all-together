#!/usr/bin/env python3

class Shoe:
     def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"  # Initialize condition attribute

     @property
     def size(self):
        return self._size

     @size.setter
     def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value
     def cobble(self):
        self.condition = "New"  # Update condition after repair
        print("Your shoe is as good as new!")