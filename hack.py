import time
import random

def hack_simulation():
    print("Hacking into the mainframe...")
    time.sleep(2)
    
    print("Bypassing firewalls...")
    time.sleep(2)
    
    print("Accessing encrypted data...")
    time.sleep(2)
    
    print("Injecting malicious code...")
    time.sleep(2)
    
    print("Hacking complete! System compromised.")
    time.sleep(1)
def matrix_effect(lines=20):
    symbols = "!@#$%^&*()_-+=~`<>,.?/:;{}[]|"
    
    for _ in range(lines):
        line = ''.join(random.choice(symbols) for _ in range(40))
        print(line)
        time.sleep(0.1)

hack_simulation()
matrix_effect()
