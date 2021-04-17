# NLU

The only requirements for this assignement are Spacy and the pipeline en_core_web_sm. They can be downloaded:

- **using pip:**
  ```
  pip install -U spacy
  python -m spacy download en_core_web_sm
  ```
  
- **using conda:**
  ```
  conda install -c conda-forge spacy
  python -m spacy download en_core_web_sm
  ```
  
- **from source:**
  ```
  pip install -U pip setuptools wheel
  git clone https://github.com/explosion/spaCy
  cd spaCy
  pip install -r requirements.txt
  python setup.py build_ext --inplace
  pip install .
  python -m spacy download en_core_web_sm
  ```
