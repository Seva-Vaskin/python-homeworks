import sys
from pathlib import Path
from latex_generator_test.latex_generator import *


@gen_document(["graphicx"])
def create_latex_code(table, image_path):
    res = [latex_scope("centering")(generate_latex_table)(table)]
    res += [generate_latex_image(image_path, scale=0.1)]
    return '\n'.join(res)


def main():
    assert len(sys.argv) == 4, "Usage: python script.py <rows> <columns> <image_path>"
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    image_path = Path(sys.argv[3])
    table = [[i + j for j in range(m)] for i in range(n)]

    print(create_latex_code(table, image_path))


if __name__ == "__main__":
    main()
