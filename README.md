## add_hash.py program

Purpose: to make a unique filename for a PDF, starting with a LaTeX file. The goal is to prevent anyone from guessing how to find alternate versions of the document in the same directory.

To set up:

 1. Install Python 3, `pip` for Python 3,  and `pyvenv`.
 1. Create and populate a Python virtual environment (one-time step):

    ```bash
    pyvenv v_env3
    . v_env3/bin/activate
    pip install -Ur requirements.txt
    ```
 1. Activate virtual environment:

    ```bash
    . v_env3/bin/activate
    python add_hash.py <path to .tex file>
    ```
    
    The `.tex` file should be in a subdirectory, specified in `<path to .tex file>`. The program will 
    
    2. calculate a hash value of the whole `.tex` file
    2. generate a PDF of the `.tex` file using `xelatex`
    2. append the hash to the filename of the PDF and save it in the main directory
    2. leave the original `.tex` file untouched in its subdirectory
    2. delete all auxiliary tex files.

 1. If a PDF with the expected filename already exists, the program will exit and the files will be untouched.

[end]

