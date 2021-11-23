# usage in cmd-line: python <name_of_this_file> <name_of_brainfuck_file>
# the brainfuck file must be in the same directory
# python brainfuck.py example.bf

# usage as module: import brainfuck

# code = ",.,."
# brainfuck.interpret(code)

# (brainfuck must be replaced with the name of this file (without .py)) brainfuck.py -> brainfuck

import sys


def clean_code(code: str) -> str:
    """returns a cleaned version of the given code"""
    used_chars = ["<", ">", "+", "-", ",", ".", "[", "]"]
    return "".join(filter(lambda char: char in used_chars, code))

def build_loop_dict(code: str) -> dict:
    """builds a helper dictionary for all loops in the
    given bf code (matches all opening '[' indexes to it's closing ']' indexes
    and all closing ']' indexes to it's opening '[' indexes)."""
    open_loops = []
    loops = {}

    for pos, char in enumerate(code):        
        if char == "[":
            open_loops.append(pos)
        elif char == "]":
            start = open_loops.pop()
            loops[start] = pos
            loops[pos] = start
    
    return loops

def interpret(code: str) -> None:
    """interprets the given bf code"""
    code = clean_code(code)
    loops = build_loop_dict(code)

    cell_ptr, code_ptr = 0, 0
    cells = [0]
    
    while code_ptr < len(code):
        
        match code[code_ptr]:

            case ">":
                cell_ptr += 1
                if len(cells) <= cell_ptr:
                    cells.append(0)

            case "<":
                cell_ptr = cell_ptr - 1 if cell_ptr > 0 else 0
            
            case "+":
                cells[cell_ptr] = cells[cell_ptr] + 1 if cells[cell_ptr] < 255 else 0
                
            case "-":
                cells[cell_ptr] = cells[cell_ptr] - 1 if cells[cell_ptr] > 0 else 255
                
            case ".":
                print(chr(cells[cell_ptr]), end="")
            
            case ",":
                cells[cell_ptr] = ord(input())
            
            case "[" if cells[cell_ptr] == 0:
                code_ptr = loops[code_ptr]

            case "]" if cells[cell_ptr] != 0:
                code_ptr = loops[code_ptr]

        code_ptr += 1

def interpret_file(filename: str) -> None:
    """reads the file with the given filename
    and interprets it's content"""
    with open(filename, "r") as file:
        interpret(file.read())



if __name__ == "__main__":
    arguments = sys.argv

    if len(arguments) >= 2:
        interpret_file(arguments[1])
        
        

        