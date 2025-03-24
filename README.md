# install

    pip install -r requirements.txt

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
