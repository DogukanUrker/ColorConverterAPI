from flask import Flask  # Import the Flask module for creating the API

app = Flask(__name__)  # Create a Flask application

class HexConverter:
    @staticmethod
    def hexToRgb(hexCode):
        # Remove the '#' character from the hex code
        hexCode = hexCode.lstrip('#')
        
        # Convert the hex code to RGB values
        # by splitting it into three parts (red, green, blue)
        # and converting each part from hexadecimal to decimal
        rgb = tuple(int(hexCode[i:i+2], 16) for i in (0, 2, 4))
        
        # Return the RGB values as a tuple
        return rgb

    @staticmethod
    def hexToRgba(hexCode, alpha):
        # Convert the hex code to RGB values
        rgb = HexConverter.hexToRgb(hexCode)
        
        # Create a new tuple by adding the alpha value to the RGB values
        rgba = rgb + (alpha,)
        
        # Return the RGBA values as a tuple
        return rgba


class RGBConverter:
    @staticmethod
    def rgbToHex(rgb):
        # Convert the RGB values to a hex code
        # by formatting the values as hexadecimal strings
        # and concatenating them with the '#' character
        hexCode = '#{:02x}{:02x}{:02x}'.format(*rgb)
        
        # Return the hex code
        return hexCode

    @staticmethod
    def rgbToRgba(rgb, alpha):
        # Create a new tuple by adding the alpha value to the RGB values
        rgba = rgb + (alpha,)
        
        # Return the RGBA values as a tuple
        return rgba


class RGBAConverter:
    @staticmethod
    def rgbaToRgb(rgba):
        # Extract the RGB values from the RGBA values
        rgb = rgba[:3]
        
        # Return the RGB values as a tuple
        return rgb

    @staticmethod
    def rgbaToHex(rgba):
        # Convert the RGBA values to RGB values
        rgb = RGBAConverter.rgbaToRgb(rgba)
        
        # Convert the RGB values to a hex code
        hexCode = RGBConverter.rgbToHex(rgb)
        
        # Return the hex code
        return hexCode

@app.get("/")  # Decorator to define the route for the home page
def home():
    return "Welcome to the Color Converter API!"  # Return a welcome message when the home page is accessed

@app.get("/convert/hex/rgb/<hexCode>")  # Decorator to define the route for converting hex to RGB
def hexToRgb(hexCode):
    rgb = HexConverter.hexToRgb(hexCode)  # Call the hexToRgb method from the HexConverter class
    return {"rgb": rgb}  # Return the RGB value as a JSON object

@app.get("/convert/hex/rgba/<hexCode>/<alpha>")  # Decorator to define the route for converting hex to RGBA
def hexToRgba(hexCode, alpha):
    rgba = HexConverter.hexToRgba(hexCode, float(alpha))  # Call the hexToRgba method from the HexConverter class
    return {"rgba": rgba}  # Return the RGBA value as a JSON object

@app.get("/convert/rgb/hex/<r>/<g>/<b>")  # Decorator to define the route for converting RGB to hex
def rgbToHex(r, g, b):
    rgb = (int(r), int(g), int(b))  # Convert the RGB values to integers
    hexCode = RGBConverter.rgbToHex(rgb)  # Call the rgbToHex method from the RGBConverter class
    return {"hex": hexCode}  # Return the hex code as a JSON object

@app.get("/convert/rgb/rgba/<r>/<g>/<b>/<alpha>")  # Decorator to define the route for converting RGB to RGBA
def rgbToRgba(r, g, b, alpha):
    rgb = (int(r), int(g), int(b))  # Convert the RGB values to integers
    rgba = RGBConverter.rgbToRgba(rgb, float(alpha))  # Call the rgbToRgba method from the RGBConverter class
    return {"rgba": rgba}  # Return the RGBA value as a JSON object

@app.get("/convert/rgba/rgb/<r>/<g>/<b>/<alpha>")  # Decorator to define the route for converting RGBA to RGB
def rgbaToRgb(r, g, b, alpha):
    rgba = (int(r), int(g), int(b), float(alpha))  # Convert the RGBA values to integers and float
    rgb = RGBAConverter.rgbaToRgb(rgba)  # Call the rgbaToRgb method from the RGBAConverter class
    return {"rgb": rgb}  # Return the RGB value as a JSON object

@app.get("/convert/rgba/hex/<r>/<g>/<b>/<alpha>")  # Decorator to define the route for converting RGBA to hex
def rgbaToHex(r, g, b, alpha):
    rgba = (int(r), int(g), int(b), float(alpha))  # Convert the RGBA values to integers and float
    hexCode = RGBAConverter.rgbaToHex(rgba)  # Call the rgbaToHex method from the RGBAConverter class
    return {"hex": hexCode}  # Return the hex code as a JSON object

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask application in debug mode if the script is executed directly
