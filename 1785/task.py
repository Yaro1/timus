import sys

def main():
    name_numbers = [
        (4, "few"), (9, "several"), (19, "pack"), 
        (49, "lots"), (99, "horde"), (249, "throng"), 
        (499, "swarm"), (999, "zounds"), (float("inf"), "legion")
    ]
    num = int(input())
    for number, name in name_numbers:
        if num <= number:
            print(name)
            break
    

if __name__ == "__main__":
    main()