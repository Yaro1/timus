import sys

def main():
    a = input()
    b = input()
    print("yes" if int(a) % 2 == 0 or int(b) % 2 == 1 else "no")
    

if __name__ == "__main__":
    main()