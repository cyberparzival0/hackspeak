# Hacker Speak
- Literacy for the technical illiterate

## Fight Club Rules
- Never say hacker!
- Never use the words violate, compromise, break, exploit, etc.
- Never use your real IP addresses.
- And always use leetspeak in the chat room.

## Why
- (Author) Because who really invented English anyways???
- (Real World) But there's like a legit book and like it's the dictionary
- (Author) But who invented it!!! 

## Main Program - hackerspeak.py
* `from hackerspeak import LeetSpeak` - Importing hackerspeak.
* `translation = LeetSpeak()` - Instantiate the class.
* `translation.printCodePage()` - Print the dictionary mapping.
* `translation.encode(msg)` - Encode a message you want in Pseudo leetspeak.
* `translation.decode(encodedMsg)` - Decode a message that was encoded by this package.

## Dragons Beware
- Wrote the code on Ubuntu
- Pseudo leetspeak as it changes all the characters to lowercase, and replaces all periods with excla
mations. Might fix later, shouldn't be that bad. Also, encoded the leetspeak with a dot between each
character for readability.
- Because of these limitations, it is recommended to only use on English plaintext.
