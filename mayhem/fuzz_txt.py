#! /usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from cleantext import clean


@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    try:
        clean(fdp.ConsumeString(200), fdp.ConsumeBool(), fdp.ConsumeBool(), fdp.ConsumeBool(), fdp.ConsumeBool(),
              fdp.ConsumeBool(), fdp.ConsumeBool(), fdp.ConsumeBool(), fdp.ConsumeBool(),
              fdp.ConsumeBool(), fdp.ConsumeBool(), fdp.ConsumeBool())

    except ValueError:
        pass


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
