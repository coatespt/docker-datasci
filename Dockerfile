FROM python:3

WORKDIR /usr/src/app

COPY ./requirements.txt ./

COPY ./install_packages.sh ./

COPY ./flask_app.py ./

COPY ./setup.sh ./

RUN ./install_packages.sh .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "python", "./app.py" ]
CMD [ "/bin/bash" ]
