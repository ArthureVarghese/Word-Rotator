# Word-Rotator
A simple Python Script to Rotate Letters of words [from a-z]

## Usage

```bash
usage: solver.py [-h] [-i FILENAME] [-t TEXT] [-o OUTPUTFILENAME] [-n NUMBER] [-r {f,b}]                                
Rotate Letters

options:
  -h, --help            show this help message and exit
  -i FILENAME, --input FILENAME
                        input file
  -t TEXT, --text TEXT  Plain Text
  -o OUTPUTFILENAME, --output OUTPUTFILENAME
                        output file name
  -n NUMBER, --number NUMBER
                        Rotation Number
  -r {f,b}, --rotation {f,b}
                        rotation direction f = forward b = backward
```

Suppose that your Python 3 interpreter is ``python`` and the text is stored in ``file.txt`` then run the script by : 
```bash
python solver.py -i /path/to/my/file.txt
```
### Output

The Default output will be printed on Command Line and will be Backward 26 rotations

To get output in a file use : ``-o filename``

To get forward rotation use : `` -r f ``

To get specific rotation use : ``-n number``
