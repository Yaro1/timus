import sys

def main():
    operations = ['+', '-', '*']
    l = [int(input()), int(input()), int(input())]
    ans = float("inf")
    for i in operations:
        for j in operations:
            ans = min(eval(f"{l[0]}{i}{l[1]}{j}{l[2]}"), ans)
    print(ans)

    

if __name__ == "__main__":
    main()