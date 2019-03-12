# Sentence Generator From Whatsapp Chat
This program takes your whatsapp chat dump and generates artificial sentences according to your language usage.

## How it does, What it does
Program uses language modeling with 3-grams. It starts with random sample from your vocabulary, and predicts next word according to last 2 words. 
It just samples from the probability distribution of words. 
Important thing is that to get nice and not-copied (but artificially generated) sentences, you need to feed long chat. 
A 300k line of chat must be enough to get artificial sentences. For shorter chats you get sentences more look like copy of what you really wrote, instead of generated.

## Installation & Run
### To install
- Run the following commands on your terminal after you set your current directory to desired folder: 
- `git clone https://github.com/polatbilek/Sentence-Generator-From-Whatsapp-Chat.git`
- `cd Sentence-Generator-From-Whatsapp-Chat`
- `python3 bot.py -l 6 -p \*_path-to-your-whatsapp-dump_*/ -name \*name-of-the-whatsapp-user*/` or `python bot.py -l 6 -p \*path-to-your-whatsapp-dump*/ -name \*name-of-the-whatsapp-user*/`
    e.g. (python3 bot.py -l 6 -p \home\myusername\Desktop\_chat.txt -name Polatbilek)

### To run
- `-l` argument stands for length of the sentence you want to generate
- `-p` argument is the absolute path to the chat file
- `-name` argument stands for the name of the user that you want to model. If you type "all" as name it takes all users in the chat (useful in group chats when you want to model the group's language)
- To get whatsapp chat dump from whatsapp, you simply touch to the name of the user or group in chat.
When you get details scroll down you will see "extract/export the chat" or something like that, with that option you can get the dump.
You can search further on the internet about how to export the chat, if the option changes or you fail to do that.

## Requirements
- Python 3.x
- NLTK
- numpy
