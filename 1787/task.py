import sys

def main():
    k, n = input().split()
    k = int(k)
    a = [int(i) for i in input().split()] + [0]
    curr_cnt = 0
    for i in range(len(a) - 1):
        if a[i] > k:
            a[i + 1] += a[i] - k
    print(a[-1])
    

if __name__ == "__main__":
    main()