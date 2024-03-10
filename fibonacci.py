#!/usr/bin/env python3
import time
import signal

running = True
licznik = 0
def handle_sigint(signum, frame):
    return True

def handle_sigterm(signum, frame):
    print(licznik)
    if licznik<100:
	print("za mało obliczeń");
    running = False

def main():

    signal.signal(signal.SIGINT, handle_sigint)
    signal.signal(signal.SIGTERM, handle_sigterm)

    num1 = 0
    num2 = 1
    next_number = num2
    while running:
        print(f"{next_number}")
        num1, num2 = num2, next_number
        next_number = num1 + num2
        licznik = licznik + 1
        time.sleep(1)

if __name__ == '__main__':
    main()