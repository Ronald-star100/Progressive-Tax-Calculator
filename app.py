# Task 1: My tax brackets:
# 5.8% up to $18,750
# 12.4% from $18,750 to $64,250
# 20.7% over $64,250

from flask import Flask, render_template, request

app = Flask(__name__)


# Task 2: Show the form.
@app.route("/")
def index():
    return render_template("index.html")


# Tasks 2–4: Calculate and show the tax.
@app.route("/calculate", methods=["POST"])
def calculate():
    income_text = request.form.get("income", "")
    try:
        income = float(income_text)
    except ValueError:
        return render_template(
            "index.html",
            error="please enter a valid income."
        )

    # Task 4: Don't allow negative income.
    if income < 0:
        return render_template(
            "index.html",
            error="Income cannot be negative."
        )

    # Task 2: Calculate tax for each bracket.
    if income <= 18750:
        tax = income * 0.058
    elif income <= 64250:
        tax = (18750 * 0.058) + ((income - 18750) * 0.124)
    else:
        tax = (
            (18750 * 0.058)
            + ((64250 - 18750) * 0.124)
            + ((income - 64250) * 0.207)
        )

    # Task 3: Show both amounts as dollars and cents.
    income_display = f"${income:.2f}"
    tax_display = f"${tax:.2f}"

    return render_template(
        "result.html",
        income=income_display,
        tax=tax_display
    )


if __name__ == "__main__":
    app.run(debug=True)