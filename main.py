import re
from utils import (stacks, bancodes)
from patterns import (url_pattern, bancode_pattern)

def validate_url(input_string):
    """Validate URL in entire input string"""
    return bool(re.match(url_pattern, input_string))

def validate_bancodes(input_string):
    """Validate Bancodes in entire input string"""
    input_pattern = r'^(' + bancode_pattern + r' ?)*$'
    return bool(re.match(input_pattern, input_string))

def validate_justice(input_string):
    "Checks if Bancodes and provided URL are correct"
    # Split the input string into lines
    lines = input_string.strip().split("\n")
    # Validate each line
    for line in lines:
        line = line.strip()
        if not validate_url(line) and not validate_bancodes(line):
            return False
    return True

for stack in stacks: # Performs action for each stack (runs for loop: runs for each stack)
    for url in stack: # Performs action for each url (runs for loop: runs for each url)
        print(f"Stack {stacks.index(stack)} / URL {stack.index(url)}") # Highlight Stack No. and URL No of that stack.
        for bancode in bancodes: # Performs action for each stack (runs for loop: runs for each bancode)
            ban_string = bancode + "\n" + url # Link should be entered in the next line of the codes
            attempt = validate_justice(ban_string) # Attempts to check if given gban string is correct
            print( # Logs the data
                f"status: {'Success' if attempt else 'Failed'} | " \
                f"BanCode: [{bancodes.index(bancode)}]({bancode}) | " \
                f"URL [{stacks.index(stack)}/{stack.index(url)}]({url})"
            )
        print("==============================\n")
    print("\n\n\n")