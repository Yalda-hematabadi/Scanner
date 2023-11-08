class SymbolTable:
    def __init__(self):
        self.size = 100
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


keywords = [("id","write"), ("id","read"), ("id","loop"), ("id","until"), ("id","if"), ("id","so"), ("OpPr", "("), ("ClPr", ")"), ("SC",";"),
            ("OpBr", "["), ("ClBr", "]"), ("mod", "%"), ("division","/"), ("sub","-"), ("sum", "+"), ("star","*"), ("equal","=="), ("assignment", "=")]

symbol_table = SymbolTable()

for key, value in keywords:
    symbol_table.insert(key, value)

print(symbol_table.table)