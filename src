import math

# Rectangle: area and perimeter
def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Circle: area and circumference
def circle_area(radius):
    return math.pi * radius * radius

def circle_perimeter(radius):
    return 2 * math.pi * radius

if __name__ == "__main__":
    print("Area & Perimeter Calculator (Sprint 1 Prototype)")
    print("Choose shape: 1) Rectangle  2) Circle")
    choice = input("Enter choice: ")

    if choice == "1":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print(f"Rectangle Area = {rectangle_area(l, w):.2f}")
        print(f"Rectangle Perimeter = {rectangle_perimeter(l, w):.2f}")

    elif choice == "2":
        r = float(input("Enter radius: "))
        print(f"Circle Area = {circle_area(r):.2f}")
        print(f"Circle Circumference = {circle_perimeter(r):.2f}")

    else:
        print("Invalid choice.")
