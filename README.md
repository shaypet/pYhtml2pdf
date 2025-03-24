## create exe

    pyinstaller --onefile --add-data "bin/wkhtmltopdf.exe;bin" script.py

# run

### make sure all files are next to the exe. else, change in the code

    script.exe input.html out.pdf
