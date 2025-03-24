# install

tested on Python 3.8.0

    python -m venv .
    pip install -r requirements.txt

# run script

    python script.py templates/v1/input.html pdf/out.pdf

## create exe

    pyinstaller --onefile --add-data "bin/wkhtmltopdf.exe;bin" script.py

## recommended folder structure

```
.
├── script.exe
└── templates
    └── v1
        ├── fonts
        │   └── font.ttf
        ├── input.html
        ├── styles.css
        └── pic.jpg
```

# run

### make sure all files are next to the exe. else, change in the code

    script.exe templates/v1/input.html pdf/out.pdf
