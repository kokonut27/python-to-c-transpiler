f = open("index.py")
r = f.readlines()
unknown_var_name_num = 0

# c libs
# you have to be able to translate python libraries/modules that are similar to c libraries
def clibs(filename):
  clibslist = open('clibs.txt') # no open source libraries, only builtin.
  string = "#include <placeholder.h>"
  for libs in clibslist:
    if filename in libs:
      string = string.replace("placeholder", filename)
      return string

# data types + functions
'''
str -> string
str (if one character) -> char 
int -> int or char
signed int -> int
unsigned int -> non-negative int
float -> float
float -> double
'''
class data_types:
  def __init__(self, text):
    self.text = text

  def str_to_char(self, string_func): # problem is i have to be able to identify whether a data is a string through looking for quotation marks or numbers, etc.
    if string_func: # this means they used the str function
      right_paren_index = self.text.find(')')
      self.text = self.text.replace("str('", "char ")
      self.text = self.text.replace("')", ";")
      self.text = self.text.replace('str("', "char ")
      self.text = self.text.replace('")', ";")
      try:
        equal_sign_index = self.text.find("=")
        var_name_exists = True
      except:
        var_name_exists = False
  
      if var_name_exists != True:
        var_name = 'var' + str(unknown_var_name_num)
        unknown_var_name_num += 1
      else:
        var_name = self.text[0:equal_sign_index]
        var_name = var_name.replace(' ', '')

      str_index = self.text.find('str(')
      value = self.text[str_index+4:right_paren_index]

      syntax = 'char ' + var_name + '[] = "' + value + '";'
      return syntax
    else: # this means it is a regular string which is just quotations which is something c doesn't have.
      pass
      
    # check if there is a variable name before the str, then apply to char
    # syntax: var = str(string) -> char var[] = "string";
    # by default, make every variable named var (and then go up by 1 number by each variable)
    

# main processor
running = True
while running:
  for line in r:
    # insert c libs first by alphabetical order
    # if "___" in line: print(clibs('assert'))
    if "print(" in line or "input(" in line: 
      print(clibs('stdio'))
    if 'str(' in line:
      print(data_types(line).str_to_char(True))
    if '"' in line:
      data_types(line).str_to_char(False)
    
    # remember the semi-colons to insert at the end

    # remember to translate colons into brackets

  running = False