# Build Stage
FROM fuzzers/atheris:2.0.7-python3.9

# Install dependencies

ADD . /src
WORKDIR /src
RUN python3 -m pip install .
RUN pip install clean-text[gpl,sklearn]
RUN pip install clean-text[sklearn]

CMD ["/src/mayhem/fuzz_txt.py"]
