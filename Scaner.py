#TODO دیاگرام حالت

import re

class SymbolTable:
    def __init__(self):
        self.size = 30
        self.table = [None] * self.size

    def _hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def insert(self, key, value):
        hash_value = self._hash(key)
        if self.table[hash_value] is None:
            self.table[hash_value] = (key, value)

    def lookup(self, key):
        hash_value = self._hash(key)
        if self.table[hash_value] is not None:
            return self.table[hash_value]

        return None



class Scanner:
    def __init__(self):
        return



keywords = [("id",r"write"), ("id",r'read'), ("id",r"loop"), ("id",r"until"), ("id",r"if"), ("id",r"so"), ("OpPr", r'('), ("ClPr", r")"), ("SC",r";"),
            ("OpBr", r"["), ("ClBr", r"]"), ("mod", r"%"), ("division",r"/"), ("sub",r"-"), ("sum", r"+"), ("star",r"*"), ("equal",r"=="), ("assignment", r"=")]

# symbol_table = SymbolTable()

# for key, value in keywords:
#     symbol_table.insert(key, value)

# print(symbol_table.table)