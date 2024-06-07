import re
from utils import (stacks, bancodes)
from patterns import (url_pattern, bancode_pattern)

def validate_url(input_string) -> bool:
    """Validate URL in entire input string"""
    return bool(re.match(url_pattern, input_string))

def validate_bancodes(input_string) -> bool:
    """Checks if given string checks the following conditions:
    {(Prefix)x(Bancode Number)}
    Telegram or Telegraph URL

    Example:
    {SXSx21} {UXx15} {OZx12}
    t.me/c/1375161034/4
    t.me/chatusername/4
    telegram.me/c/1375161034/4
    telegram.me/chatusername/4
    telegram.dog/c/1375161034/4
    telegram.dog/chatusername/4
    graph.org/file/d7a4a7f2f0f6d1d
    te.legra.ph/file/d7a4a7f2f0f6d1d
    telegra.ph/file/d7a4a7f2f0f6d1d
    https://t.me/c/1375161034/4
    https://t.me/chatusername/4
    https://telegram.me/c/1375161034/4
    https://telegram.me/chatusername/4
    https://telegram.dog/c/1375161034/4
    https://telegram.dog/chatusername/4
    https://graph.org/file/d7a4a7f2f0f6d1d
    https://te.legra.ph/file/d7a4a7f2f0f6d1d
    https://telegra.ph/file/d7a4a7f2f0f6d1d
    """
    input_pattern = r'^(' + bancode_pattern + r' ?)*$'
    return bool(re.match(input_pattern, input_string))

def validate_justice(input_string) -> bool:
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