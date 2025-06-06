import cv2
import numpy as np
import easyocr

reader = easyocr.Reader(['en'])  # English language

def process_screenshot(image_path: str) -> list[str]:
    """
    Preprocesses image and runs EasyOCR on it to detect text and split into the tiles. 
    """
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return []

    height, width, _ = img.shape

    bottom_half = img[height//2:, :]
    gray = cv2.cvtColor(bottom_half, cv2.COLOR_BGR2GRAY)

    scale_factor = 2
    resized = cv2.resize(gray, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    
    sharpened = cv2.filter2D(resized, -1, kernel)

    _, thresh = cv2.threshold(sharpened, 150, 255, cv2.THRESH_BINARY)
    cv2.imwrite("processed_image.png", thresh)

    results = reader.readtext(thresh, detail=0)

    lines = [line.strip().lower() for line in results if line.strip()]

    processed_lines: list[str] = []
    for idx, text in enumerate(lines):
        processed_lines.append(text)
        print(f"Line {idx + 1}: '{text}'")

    tiles: list[str] = []
    for line in processed_lines:
        words = line.split(' ')
        for word in words:
            tiles.append(word)

    return tiles

if __name__ == "__main__":
    output = process_screenshot("tests/screenshot2.jpg")
    print("Extracted Text Lines:", output)

