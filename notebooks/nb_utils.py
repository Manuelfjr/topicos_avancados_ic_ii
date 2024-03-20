import sys
from pathlib import Path
from typing import Union


def set_root(level: int = 1, return_path: bool = False) -> Union[str, None]:
    for i in range(level):
        if i == 0:
            PROJECT_DIR = Path.cwd().parent
        else:
            PROJECT_DIR = PROJECT_DIR.parent
    sys.path.append(PROJECT_DIR)
    if return_path:
        return PROJECT_DIR
    else:
        return None
