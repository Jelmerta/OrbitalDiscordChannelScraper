from python:latest

WORKDIR /home

COPY orbital.py ./

RUN python3 -m pip install --user --upgrade git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum

CMD [ "python3", "./orbital.py" ]
