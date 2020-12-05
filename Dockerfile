FROM python:3
WORKDIR /usr/src/app
COPY ./requirements.txt ./
COPY ./install_packages.sh ./
# COPY ./app.py ./
COPY ./setup.sh ./
RUN ./install_packages.sh .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# CMD [ "/bin/bash" ]
# CMD [ "python", "./app.py" ]
CMD [ "/bin/bash" ]
