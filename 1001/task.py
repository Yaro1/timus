import sys

def main():
    ans = []
    for line in sys.stdin:
        nums = line.split()
        for num in nums:
            ans.append(int(num) ** 0.5)
    for item in ans[::-1]:
        print("%.4f" % item)

if __name__ == "__main__":
    main()