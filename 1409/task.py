import sys

def main():
    a, b = input().split()
    c = min(int(a) + int(b) - 1, 10)
    print(c - int(a), c - int(b))
    

if __name__ == "__main__":
    main()