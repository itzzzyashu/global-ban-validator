import re
from patterns import (url_pattern, bancode_pattern)

def validate_url(input_string) -> bool:
   return bool(re.match(url_pattern, input_string))

def validate_bancodes(input_string) -> bool:
   input_pattern = r'^(' + bancode_pattern + r' ?)*$'
   return bool(re.match(input_pattern, input_string))

def validate_justice(input_string) -> bool:
   lines = input_string.strip().split("\n")
   for line in lines:
      line = line.strip()
      if not validate_url(line) and not validate_bancodes(line):
         print(f"Error in line of string: {line}")
         return False
      print(f"Valid ({line})")
   return True

attempt = validate_justice(ban_string)
print(f"\n\nstatus: {'Success' if attempt else 'Failed'}")