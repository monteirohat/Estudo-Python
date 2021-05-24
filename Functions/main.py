from utils import *


list_functions = {
    "1": "abs()",
    "2": "all()",
    "3": "any()",
    "4": "ascii()",
    "5": "bin()",
    "6": "bool()",
    "7": "breakpoint()",
    "8": "bytearray()",
    "9": "bytes()",
    "10": "callable()",
    "11": "chr()",
    "12": "classmethod()",
    "13": "compile()",
    "14": "complex()",
    "15": "delattr()",
    "16": "dict()",
    "17": "dir()",
    "18": "divmod()",
    "19": "enumerate()",
    "20": "eval()",
    "21": "exec()",
    "22": "filter()",
    "23": "float()",
    "24": "format()",
    "25": "frozenset()",
    "26": "getattr()",
    "27": "globals()",
    "28": "hasattr()",
    "29": "hash()",
    "30": "help()",
    "31": "hex()",
    "32": "id()",
    "33": "input()",
    "34": "int()",
    "35": "isinstance()",
    "36": "issubclass()",
    "37": "iter()",
    "38": "len()",
    "39": "list()",
    "40": "locals()",
    "41": "map()",
    "42": "max()",
    "43": "memoryview()",
    "44": "min()",
    "45": "next()",
    "46": "object()",
    "47": "oct()",
    "48": "open()",
    "49": "ord()",
    "50": "pow()",
    "51": "print()",
    "52": "property()",
    "53": "range()",
    "54": "repr()",
    "55": "reversed()",
    "56": "round()",
    "57": "set()",
    "58": "setattr()",
    "59": "slice()",
    "60": "sorted()",
    "61": "staticmethod()",
    "62": "str()",
    "63": "sum()",
    "64": "super()",
    "65": "tuple()",
    "66": "type()",
    "67": "vars()",
    "68": "zip()",
    "69": "__import__()"
}

print("*"*100)
print("Author: André Monteiro")
print("Description: Examples of using the 69 Python functions")
print("*"*100)
print()
print("==> Choose a function:")
print()

count = 0
new_line = False
text_line = ""
matrix_line = ""
matrix_col = ""

for i in list_functions:

    if count == 14:
        new_line= True
        count = 0


    if not new_line:
        matrix_col += f"{i}  - {list_functions[i]}" 
    else:
        matrix_line += f"{i}  - {list_functions[i]}"
    
    count +=1


print(matrix_col)
#print(matrix_line)













































# print("1 - abs()", space_table(), "15 - delattr()",
#       space_table(), "29 - hash()", space_table(), "43 - memoryview()",
#       space_table(), "57 - set()")
# print("2 - all()", space_table(), "16 - dict()",
#       space_table(), "30 - help()", space_table(), "44 - min()",
#       space_table(), "58 - setattr()")
# print("3 - any()", space_table(), "17 - dir()",
#       space_table(), "31 - hex()", space_table(), "45 - next()",
#       space_table(), "59 - slice()")

print("_"*100)
