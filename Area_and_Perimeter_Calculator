import math

# --- Geometry Functions ---
def rectangle_area(length, width): return length * width
def rectangle_perimeter(length, width): return 2 * (length + width)

def circle_area(radius): return math.pi * radius ** 2
def circle_perimeter(radius): return 2 * math.pi * radius

def square_area(side): return side ** 2
def square_perimeter(side): return 4 * side

def triangle_area(base, height): return 0.5 * base * height
def triangle_perimeter(a, b, c): return a + b + c

def parallelogram_area(base, height): return base * height
def parallelogram_perimeter(a, b): return 2 * (a + b)

# --- Input helper ---
def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Value must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# --- Shape menu dictionary ---
shapes = {
    "1": {
        "name": "Rectangle",
        "area": lambda: rectangle_area(
            get_number("Enter length: "),
            get_number("Enter width: ")
        ),
        "perimeter": lambda: rectangle_perimeter(
            get_number("Enter length again: "),
            get_number("Enter width again: ")
        )
    },
    "2": {
        "name": "Circle",
        "area": lambda: circle_area(get_number("Enter radius: ")),
        "perimeter": lambda: circle_perimeter(get_number("Enter radius again: "))
    },
    "3": {
        "name": "Square",
        "area": lambda: square_area(get_number("Enter side length: ")),
        "perimeter": lambda: square_perimeter(get_number("Enter side length again: "))
    },
    "4": {
        "name": "Triangle",
        "area": lambda: triangle_area(
            get_number("Enter base: "),
            get_number("Enter height: ")
        ),
        "perimeter": lambda: triangle_perimeter(
            get_number("Enter side a: "),
            get_number("Enter side b: "),
            get_number("Enter side c: ")
        )
    },
    "5": {
        "name": "Parallelogram",
        "area": lambda: parallelogram_area(
            get_number("Enter base: "),
            get_number("Enter height: ")
        ),
        "perimeter": lambda: parallelogram_perimeter(
            get_number("Enter side a: "),
            get_number("Enter side b: ")
        )
    }
}

# --- Main loop ---
if __name__ == "__main__":
    print("Area & Perimeter Calculator (Dictionary Version)")

    while True:
        print("\nChoose shape:")
        print("1) Rectangle  2) Circle  3) Square  4) Triangle  5) Parallelogram  6) Exit")
        choice = input("Enter choice (1-6): ")

        if choice == "6":
            print("Exiting program. Goodbye!")
            break
        elif choice in shapes:
            shape = shapes[choice]
            area = shape["area"]()
            perimeter = shape["perimeter"]()
            print(f"\n{shape['name']} Area = {area:.2f}")
            print(f"{shape['name']} Perimeter = {perimeter:.2f}")
        else:
            print("Invalid choice. Please select 1-6.")
