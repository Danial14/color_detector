from colorgram import extract
import webcolors, json
filePath = ""
extractedColors = None
def updateFilepathAndExtractColors(path):
    global filePath, extractedColors
    if isinstance(path, str):
        filePath = path
        if filePath != "":
            extractedColors = extractColorsFromImage()
            return True
        else:
            return False
    else:
        return False

def extractColorsFromImage():
    try:
        print(f"filepath is {filePath}")
        return extract(filePath, number_of_colors= 2 ** 32)
    except Exception as e:
        print("File not found or this is not a valid image file")

def writeColorsToJsonFile():
    parsedColors = parseColors()
    colors = {}
    if parsedColors != None:
        for parsedColor in parsedColors:
            color = getColorName(color=parsedColor)
            colors[color] = str(parsedColor)
        try:
            with open("colors.json", mode="w") as jsonFile:
                json.dump(colors, fp=jsonFile, indent=5)
                return True
            
        except Exception as e:
            return False

def parseColors():
    parsedColors = []
    if extractedColors != None:
        for color in extractedColors:
            rgbColor = color.rgb
            parsedColors.append((rgbColor.r, rgbColor.g, rgbColor.b))
        return parsedColors

def getColorName(color):
    try:
        colorName = webcolors.rgb_to_name(color)
        print(colorName)
        return colorName
    except Exception as e:
        closestColor = findClosestColor(color)
        return closestColor

def findClosestColor(rgbColor):
    r, g, b = rgbColor
    difference = {}
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        rgb_color = webcolors.hex_to_rgb(hex_value=color_hex)
        difference[sum([
            (rgb_color.red - r) ** 2,
            (rgb_color.green - g) ** 2,
            (rgb_color.blue - b) ** 2
        ]
        )
        ] = color_name
    return difference[min(difference.keys())]
