with open("file.txt", "r") as f:
    words = f.read().split()
    print(len(words))