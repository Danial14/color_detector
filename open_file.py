from tkinter import filedialog as fd
from extract_color import writeColorsToJsonFile, updateFilePath
def openFile():
    try:
        file = fd.askopenfile().name
        print(f"path: {file}")
        updateFilePath(file)
        writeColorsToJsonFile()
    except Exception as e:
        print("error")
        print(e)