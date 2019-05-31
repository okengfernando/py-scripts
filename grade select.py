
mark: int = int(input("ENter a mark to be graded:"))


if mark < 0:
    print("Enter a mark in the range 1 - 100")

elif mark > 100:
    print("Enter a mark in the range 1 - 100")

elif mark >= 85:
    if mark <= 100:
        print("D1")

elif mark >= 80:
    if mark <= 84:
        print("D2")

elif mark >= 75:
    if mark <= 79:
        print("C3")

elif mark >= 70:
    if mark <= 74:
        print("C4")

elif mark >= 60:
    if mark <= 69:
        print("C5")


elif mark >= 55:
    if mark <= 59:
        print("C6")

elif mark >= 50:
    if mark <= 54:
        print("P7")

elif mark >= 40:
    if mark <= 49:
        print("P8")

else:
    print("F9")
