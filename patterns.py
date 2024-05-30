# Define patterns
from utils import prefixes

# Define the regex pattern for a single ban code
bancode_pattern = ban_code_pattern = r'{(' + '|'.join(prefixes) + r')x(0[0-9]|1[0-9]|2[0-4])}'

# Define the regex pattern for a single URL
url_pattern = r'^(https?://)?(?:(?:t\.me|telegram\.me|telegram\.dog)/(?:c/(\d{11,})|([a-zA-Z0-9_]{5,})|([a-zA-Z0-9_]+))/(\d+)|(?:te\.legra\.ph|telegra\.ph|graph\.com)/([a-zA-Z0-9-]+))$'