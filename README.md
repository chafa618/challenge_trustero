    1. Install pyenv

    2. With pyenv, install python 3.7.5

    3. Inside the root run  ```pyenv local 3.7.5```

    4. Install pipenv using pip.

    5. Run  ```pipenv --python 3.7.5```

    6. Run  ```pipenv install```

    7. Run  ```pipenv run install_modules```
    
    8. Run ```pipenv run python -m ipykernel install --user --name=`pipenv run basename '$VIRTUAL_ENV'` ```

    9. To download fasttext model go to https://fasttext.cc/docs/en/crawl-vectors.html


