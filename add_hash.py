# add_hash.py
# David Branner
# 20150815

"""Generate a PDF named with distinctive hash, from LaTeX original."""

import hashlib
import os
import subprocess
import sys

# Read file and generate filenames.
old_filename = sys.argv[1]
old_filename_path, old_filename_file = os.path.split(old_filename)
old_filename_root, old_filename_ext = os.path.splitext(old_filename_file)
if old_filename_ext == '.tex':
    with open(old_filename, 'r') as f:
        content = f.read()
    hashed = hashlib.sha256(content.encode()).hexdigest()
    new_filename_root = old_filename_root + '_' + hashed
    # Below are the two things we need going forward.
    new_filename = new_filename_root + old_filename_ext
    pdf_name = new_filename_root + '.pdf'

    # Rename .tex file; generate PDF; restore .tex filename.
    if not os.path.exists(pdf_name):
        os.rename(old_filename, new_filename)
        subprocess.call(['xelatex', new_filename], stdout=subprocess.DEVNULL)
        print('\nFile generated:\n    {}'.format(pdf_name))
        os.rename(new_filename, old_filename)
        for ext in ['out', 'log', 'aux']:
            aux_file = new_filename_root + '.' + ext
            if os.path.exists(aux_file):
                os.remove(aux_file)
        print('    Auxiliary files deleted.')
    else:
        print('    File already exists:\n    {}'.format(pdf_name))
else:
    print('    Input file must end in .tex; aborting.')

