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
                a = float(request.form["A"])
                b = float(request.form["B"])
                c = float(request.form["base"])
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
    <html>
    <head>
        <title>Area & Perimeter Calculator</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f2f2f2; padding: 20px; }
            h2 { text-align: center; }
            .card { background: #fff; padding: 20px; margin: 15px auto; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); width: 300px; }
            form input { width: 100%; padding: 5px; margin: 5px 0; }
            button { background-color: #4CAF50; color: white; border: none; padding: 8px 12px; border-radius: 5px; cursor: pointer; }
            button:hover { background-color: #45a049; }
            p { margin: 5px 0; }
            .error { color: red; }
        </style>
    </head>
    <body>
        <h2>Area & Perimeter Calculator</h2>

        {% for shape_name, form_fields in [('rectangle',['length','width']),
                                           ('circle',['radius']),
                                           ('square',['side']),
                                           ('triangle',['a','b','c','h']),
                                           ('parallelogram',['base','height','a','b'])] %}

            <div class="card">
                <h3>{{ shape_name.capitalize() }}</h3>
                <form method="post">
                    <input type="hidden" name="shape" value="{{ shape_name }}">
                    {% for field in form_fields %}
                        {{ field.capitalize() }}: <input type="number" step="any" name="{{ field }}" value="{{ request.form.get(field,'') }}"><br>
                    {% endfor %}
                    <button type="submit">Calculate</button>
                </form>

                {% set res = results.get(shape_name) %}
                {% if res %}
                    {% if res.get('error') %}
                        <p class="error">{{ res.error }}</p>
                    {% else %}
                        <p>Area = {{ res.area }}, Perimeter = {{ res.perimeter }}</p>
                    {% endif %}
                {% endif %}
            </div>

        {% endfor %}
    </body>
    </html>
    """, results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
