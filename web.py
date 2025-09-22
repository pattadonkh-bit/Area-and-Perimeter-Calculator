from flask import Flask, request, render_template_string
import calculator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}

    if request.method == "POST":
        shape = request.form.get("shape")
        try:
            if shape == "rectangle":
                if not request.form["length"] or not request.form["width"]:
                    raise ValueError("กรอกให้ครบทุกช่อง")
                length = float(request.form["length"])
                width = float(request.form["width"])
                if length <= 0 or width <= 0:
                    raise ValueError("Length and width must be positive")
                results["rectangle"] = {
                    "area": calculator.rectangle_area(length, width),
                    "perimeter": calculator.rectangle_perimeter(length, width)
                }

            elif shape == "circle":
                if not request.form["radius"]:
                    raise ValueError("กรอกให้ครบทุกช่อง")
                radius = float(request.form["radius"])
                if radius <= 0:
                    raise ValueError("Radius must be positive")
                results["circle"] = {
                    "area": calculator.circle_area(radius),
                    "perimeter": calculator.circle_perimeter(radius)
                }

            elif shape == "square":
                if not request.form["side"]:
                    raise ValueError("กรอกให้ครบทุกช่อง")
                side = float(request.form["side"])
                if side <= 0:
                    raise ValueError("Side must be positive")
                results["square"] = {
                    "area": calculator.square_area(side),
                    "perimeter": calculator.square_perimeter(side)
                }

            elif shape == "triangle":
                if not request.form["a"] or not request.form["b"] or not request.form["c"] or not request.form["h"]:
                    raise ValueError("กรอกให้ครบทุกช่อง")
                a = float(request.form["a"])
                b = float(request.form["b"])
                c = float(request.form["c"])
                h = float(request.form["h"])
                if min(a, b, c, h) <= 0:
                    raise ValueError("All sides and height must be positive")
                results["triangle"] = {
                    "area": calculator.triangle_area(a, h),
                    "perimeter": calculator.triangle_perimeter(a, b, c)
                }

            elif shape == "parallelogram":
                if not request.form["base"] or not request.form["height"] or not request.form["a"] or not request.form["b"]:
                    raise ValueError("กรอกให้ครบทุกช่อง")
                base = float(request.form["base"])
                height = float(request.form["height"])
                a = float(request.form["a"])
                b = float(request.form["b"])
                if min(base, height, a, b) <= 0:
                    raise ValueError("Base, height, and sides must be positive")
                results["parallelogram"] = {
                    "area": calculator.parallelogram_area(base, height),
                    "perimeter": calculator.parallelogram_perimeter(a, b)
                }

        except (ValueError, KeyError) as e:
            results[shape] = {"error": str(e)}

    return render_template_string("""
        <h2>Area & Perimeter Calculator</h2>

        <!-- Rectangle -->
        <h3>Rectangle</h3>
        <form method="post">
            <input type="hidden" name="shape" value="rectangle">
            Length: <input type="number" step="any" name="length"><br>
            Width: <input type="number" step="any" name="width"><br>
            <button type="submit">Calculate</button>
        </form>
        {% if results.rectangle %}
            {% if results.rectangle.error %}
                <p style="color:red">{{ results.rectangle.error }}</p>
            {% else %}
                <p>Area = {{ results.rectangle.area }}, Perimeter = {{ results.rectangle.perimeter }}</p>
            {% endif %}
        {% endif %}

        <!-- Circle -->
        <h3>Circle</h3>
        <form method="post">
            <input type="hidden" name="shape" value="circle">
            Radius: <input type="number" step="any" name="radius"><br>
            <button type="submit">Calculate</button>
        </form>
        {% if results.circle %}
            {% if results.circle.error %}
                <p style="color:red">{{ results.circle.error }}</p>
            {% else %}
                <p>Area = {{ results.circle.area }}, Perimeter = {{ results.circle.perimeter }}</p>
            {% endif %}
        {% endif %}

        <!-- Square -->
        <h3>Square</h3>
        <form method="post">
            <input type="hidden" name="shape" value="square">
            Side: <input type="number" step="any" name="side"><br>
            <button type="submit">Calculate</button>
        </form>
        {% if results.square %}
            {% if results.square.error %}
                <p style="color:red">{{ results.square.error }}</p>
            {% else %}
                <p>Area = {{ results.square.area }}, Perimeter = {{ results.square.perimeter }}</p>
            {% endif %}
        {% endif %}

        <!-- Triangle -->
        <h3>Triangle</h3>
        <form method="post">
            <input type="hidden" name="shape" value="triangle">
            a: <input type="number" step="any" name="a"><br>
            b: <input type="number" step="any" name="b"><br>
            c: <input type="number" step="any" name="c"><br>
            height: <input type="number" step="any" name="h"><br>
            <button type="submit">Calculate</button>
        </form>
        {% if results.triangle %}
            {% if results.triangle.error %}
                <p style="color:red">{{ results.triangle.error }}</p>
            {% else %}
                <p>Area = {{ results.triangle.area }}, Perimeter = {{ results.triangle.perimeter }}</p>
            {% endif %}
        {% endif %}

        <!-- Parallelogram -->
        <h3>Parallelogram</h3>
        <form method="post">
            <input type="hidden" name="shape" value="parallelogram">
            Base: <input type="number" step="any" name="base"><br>
            Height: <input type="number" step="any" name="height"><br>
            Side a: <input type="number" step="any" name="a"><br>
            Side b: <input type="number" step="any" name="b"><br>
            <button type="submit">Calculate</button>
        </form>
        {% if results.parallelogram %}
            {% if results.parallelogram.error %}
                <p style="color:red">{{ results.parallelogram.error }}</p>
            {% else %}
                <p>Area = {{ results.parallelogram.area }}, Perimeter = {{ results.parallelogram.perimeter }}</p>
            {% endif %}
        {% endif %}
    """, results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
