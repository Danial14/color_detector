from extract_color import extractColorsFromImage, parseColors, getColorName, findClosestColor, writeColorsToJsonFile, updateFilePath

def testUpdateFilepath():
    assert updateFilePath("../Capture.png") == True

def testExtractColors():
    assert len(extractColorsFromImage()) > 0

def testParseColors():
    assert len(parseColors()) > 0

def testColorName():
    assert isinstance(getColorName((0, 0, 128)), str) == True

def testClosestColor():
    assert isinstance(findClosestColor((123, 12, 1)), str) == True

def testWriteColorsToJsonFile():
    assert writeColorsToJsonFile() == True
