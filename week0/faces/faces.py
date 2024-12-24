# -*- coding: utf-8 -*-
def main(text):
    return convert(text)

def convert(text : str):
    return text.replace(':)', '🙂').replace(':(', '🙁')

text=input('')

print(main(text))
