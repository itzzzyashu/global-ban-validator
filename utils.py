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
      "te.legra.ph/file/yquwyw627266242gav.png",
      "telegra.ph/file/yquwyw627266242gav.png",
      "graph.com/file/yquwyw627266242gav.png"
   ],
  
   [ # With HTTPS

      "https://te.legra.ph/file/yquwyw627266242gav.png",
      "https://telegra.ph/file/yquwyw627266242gav.png",
      "https://graph.com/file/yquwyw627266242gav.png"
   ]

]

bancodes = [
   "{UXx12} {SRSx15} {SYSx20}", #Success
   "{UXx14}", # Success
   "UXx12", # Failed
   "{UXx25}", # Failed
   "{UXx0}", # Failed
   "{UXx012}", # Failed
   "{UXx12} {SRSx15} foo" #Failed
]


# For example these URLs will be validated:
ban_string = """{SXSx21} {OZx22} {UXx15}
t.me/c/1375161034/4
t.me/chatusername/4
telegram.me/c/1375161034/4
telegram.me/chatusername/4
telegram.dog/c/1375161034/4
telegram.dog/chatusername/4
graph.org/file/d7a4a7f2f0f6d1d.png
te.legra.ph/file/d7a4a7f2f0f6d1d.png
telegra.ph/file/d7a4a7f2f0f6d1d.png
https://t.me/c/1375161034/4
https://t.me/chatusername/4
https://telegram.me/c/1375161034/4
https://telegram.me/chatusername/4
https://telegram.dog/c/1375161034/4
https://telegram.dog/chatusername/4
https://graph.org/file/d7a4a7f2f0f6d1d.png
https://te.legra.ph/file/d7a4a7f2f0f6d1d.png
https://telegra.ph/file/d7a4a7f2f0f6d1d.png"""
