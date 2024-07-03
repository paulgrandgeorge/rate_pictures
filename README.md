# rate_pictures
Python code to rate pictures (.jpg format) 



Generate virtual environment (venv) using:
python -m venv venv
pip install -r requirements.txt

Activate environement using:
.\venv\Scripts\activate
(deactivate using deactivate)

Generate standalone .exe file with 
pyinstaller --onefile --add-data C:\Users\paulg\Desktop\Rate_Pictures\venv\Lib\site-packages\pyexiv2:pyexiv2  Rate_pictures_XMP.py

Package                   Version
------------------------- --------
altgraph                  0.17.4
importlib_metadata        7.1.0
numpy                     1.26.4
packaging                 24.1
pefile                    2023.2.7
pillow                    10.3.0
pip                       24.0
pyexiv2                   2.12.0
pyinstaller               6.8.0
pyinstaller-hooks-contrib 2024.7
pywin32-ctypes            0.2.2
setuptools                58.1.0
tk                        0.1.0
zipp                      3.19.2
