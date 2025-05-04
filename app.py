from flask import Flask, render_template, request, url_for
from fractions import Fraction

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    degrees = None
    
    # Common angles reference
    common_angles = [
        {"degrees": 0, "radians": Fraction(0)},
        {"degrees": 30, "radians": Fraction(1, 6)},
        {"degrees": 45, "radians": Fraction(1, 4)},
        {"degrees": 60, "radians": Fraction(1, 3)},
        {"degrees": 90, "radians": Fraction(1, 2)},
        {"degrees": 180, "radians": Fraction(1)},
        {"degrees": 360, "radians": Fraction(2)}
    ]
    
    if request.method == 'POST':
        try:
            # Convert string input to float
            degrees = float(request.form['degrees'])
            
            # Create fraction from the float value divided by 180
            # We need to convert both parts to integers for Fraction
            # First, calculate the exact decimal value
            decimal_radians = degrees / 180
            
            # Then create the fraction from this decimal value
            radians = Fraction(decimal_radians).limit_denominator()
            
            # Format the fraction nicely for display
            if radians.numerator == 0:
                radian_display = "0"
            elif radians.denominator == 1:
                radian_display = f"{radians.numerator}"
            else:
                radian_display = f"{radians.numerator}/{radians.denominator}"
                
            result = f"{degrees} degrees is equal to {radian_display}π radians"
        except ValueError:
            result = "Please enter a valid number"
    
    return render_template('index.html', result=result, degrees=degrees, common_angles=common_angles)

if __name__ == '__main__':
    app.run(debug=True)