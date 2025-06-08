# color_analyzer.py
color_data = {"red": "#F50001", "blue": "#27A7F5", "yellow": "#F5F100"}
def analyze_colors(data):
    for color, hex_code in data.items():
        print(f"{color.capitalize()} HEX: {hex_code}")
analyze_colors(color_data)