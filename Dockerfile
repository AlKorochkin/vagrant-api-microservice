FROM python:3.7-bullseye
COPY . .
WORKDIR .
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.deb11.txt
RUN pip install python-vagrant
RUN pyinstaller --clean --onefile main.py
