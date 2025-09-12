import math

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)


def circle_area(radius):
    return math.pi * radius ** 2

def circle_perimeter(radius):
    return 2 * math.pi * radius


def square_area(side):
    return side ** 2

def square_perimeter(side):
    return 4 * side


def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(a, b, c):
    return a + b + c


def parallelogram_area(base, height):
    return base * height

def parallelogram_perimeter(a, b):
    return 2 * (a + b)

def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            num = float(value)
            if num > 0:
                return num
            else:
                print("Value must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    print("Area & Perimeter Calculator (Sprint 3)")

    while True:
        print("\nChoose shape:")
        print("1) Rectangle  2) Circle  3) Square  4) Triangle  5) Parallelogram  6) Exit")
        choice = input("Enter choice (1-6): ")

        if choice == "1":
            l = get_number("Enter length: ")
            w = get_number("Enter width: ")
            print(f"Rectangle Area = {rectangle_area(l, w):.2f}")
            print(f"Rectangle Perimeter = {rectangle_perimeter(l, w):.2f}")

        elif choice == "2":
            r = get_number("Enter radius: ")
            print(f"Circle Area = {circle_area(r):.2f}")
            print(f"Circle Circumference = {circle_perimeter(r):.2f}")

        elif choice == "3":
            s = get_number("Enter side length: ")
            print(f"Square Area = {square_area(s):.2f}")
            print(f"Square Perimeter = {square_perimeter(s):.2f}")

        elif choice == "4":
            a = get_number("Enter side a: ")
            b = get_number("Enter side b: ")
            c = get_number("Enter side c: ")
            h = get_number("Enter height (for area): ")
            print(f"Triangle Area = {triangle_area(a, h):.2f}")
            print(f"Triangle Perimeter = {triangle_perimeter(a, b, c):.2f}")

        elif choice == "5":
            base = get_number("Enter base: ")
            height = get_number("Enter height: ")
            side_a = get_number("Enter side a: ")
            side_b = get_number("Enter side b: ")
            print(f"Parallelogram Area = {parallelogram_area(base, height):.2f}")
            print(f"Parallelogram Perimeter = {parallelogram_perimeter(side_a, side_b):.2f}")

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-6.")
