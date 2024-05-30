 # Define the allowed ban code prefixes
prefixes = ['UX', 'SRS', 'SXS', 'SYS', 'OZ', 'T7']


# All these urls are validated by regex used in (./patterns.py [url_pattern: regex_string])
stacks = [

   [ # Telegram URLs without HTTPS
      "t.me/c/267252662525/671",
      "t.me/cha/12345",
      "t.me/chatusername/12345",
      "telegram.me/c/123456789012/789",
      "telegram.dog/c/267252662525/671",
      "telegram.dog/c/987654321098/321"
   ],
  
   [ # Telegram URLs with HTTP
      "https://t.me/c/267252662525/671",
      "https://t.me/cha/12345",
      "https://t.me/chatusername/12345",
      "https://telegram.me/c/123456789012/789",
      "https://telegram.dog/c/267252662525/671",
      "https://telegram.dog/c/987654321098/321"
   ],
  
   [ # Graph URLs without HTTPS
      "te.legra.ph/yquwyw6272662-42-gav",
      "telegra.ph/yquwyw6272662-42-gav",
      "telegra.ph/yquwyw6272662-42-gav",
      "graph.com/yquwyw6272662-42-gav"
   ],
  
   [ # With HTTPS

      "https://te.legra.ph/yquwyw6272662-42-gav",
      "https://telegra.ph/yquwyw6272662-42-gav",
      "https://telegra.ph/yquwyw6272662-42-gav",
      "https://graph.com/yquwyw6272662-42-gav"
   ]

]

bancodes = [
   "{UXx12} {SRSx15} {SYSx20}",
   "{UXx14}",
   "UXx12",
   "{UXx25}",
   "{UXx0}",
   "{UXx012}",
   "{UXx12} {SRSx15} foo"
]