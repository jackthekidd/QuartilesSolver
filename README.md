# Quartiles Solver

Web app that generates the solutions for Apple's Quartiles game.  
Users can manually enter tiles or upload a screenshot of the puzzle, and the app uses OCR to extract data and generate possible solutions.

---

## Features

Upload screenshots (JPG, PNG)
Automatically extract tile data using EasyOCR.  
Manually input tile data if you prefer.  
Solve the puzzle and view possible solutions.  
Web interface with Flask.

---

## Installation (If not using website)

1. **Clone this repository**:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/quartiles-solver.git
   cd quartiles-solver

2. **Optional - Create a venv**
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Installation dependencies**
    pip install -r requirements.txt

4. **Run**
    python app.py

5. **Open browser and go to**
    http://127.0.0.1:5000/

---

## Dependencies
Python 3.x
Flask
EasyOCR
OpenCV (cv2)

---

## Notes
The word list is based on Scrabble's official dictionary; Apple’s is not publicly available.

Some rare words may be missing or additional solutions might appear.

--- 

## License
MIT License
