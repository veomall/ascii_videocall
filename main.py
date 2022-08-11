import cv2
from time import sleep
import requests


def symbol(a):
    table = ' .:+a8%@'  # цветовой градиент
    b = a // 32
    return table[b]


server = input('server: ')
username = input('your username: ')
other = input('other username: ')
cap = cv2.VideoCapture(0)
q = 20/9
h = 40
w = int(40 * q * 4 / 3)
ph = 480 // h
pw = 640 // w
while True:
    frame = ''
    ret, f = cap.read()
    gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    gray = cv2.flip(gray, 1)
    for i in range(h):
        for j in range(w):
            y = ph // 2 + i * ph
            x = pw // 2 + j * pw
            frame += symbol(gray[y, x])
    requests.get(f"http://{server}/{username}/{frame}")
    response = requests.get(f"http://{server}/{other}")
    print(response.text, end='')
    frames = ''
