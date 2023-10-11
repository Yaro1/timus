import sys
import math

def main():
    n, k = map(int, input().split())
    if n < k:
        print(2)
    else:
        print(math.ceil(2*n / k))


    

if __name__ == "__main__":
    main()