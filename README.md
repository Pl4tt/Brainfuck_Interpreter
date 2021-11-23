# Brainfuck Interpreter
An interpreter for the brainfuck programming language written in python.


- Usage in command line:
  ```
  python <name_of_interpreter_file (for example "brainfuck.py")> <name_of_the_bf_file (for example "example.bf")>
  ```
- Usage as a module:
  ```python
  import brainfuck

  code = ",.,.,."
  brainfuck.interpret(code)
  ```
  or
  ```python
  import brainfuck
  
  brainfuck.interpret_file("filename.bf")  # or your own filename
  ```
  
  "brainfuck" should be replaced by the file name of the brainfuck interpreter if it was changed.
