import os
import typing

from .tempfile_ import temp

def run_xelatex(
    file : str,
):
    os.system(f"xelatex -interaction=nonstopmode {file}")

def run_xelatex_in_temp(
    folder : str,
    captures : typing.List[str]
):
    
    for file in os.listdir(folder):
        if file.endswith(".tex"):
            texFile = file
            break

    temp(
        paths = [
            folder,
        ],
        capture = captures,
    )(
        lambda: run_xelatex(texFile)
    )