num = int(input("Enter a number: "))
if num >= 0:
    def countdown(num):
        if num <= 0:
            print("Blastoff!")
        else:
            print(num, "\n")
            countdown(num - 1)

    countdown(num)

if num <= 0:
    def countup(num):
        if num >= 0:
            print("Blastoff!")
        else:
            print(num, "\n")
            countup(num + 1)

    countup(num)