import sys
from latex_generator import generate_latex_table


def main():
    assert len(sys.argv) == 3, "Usage: python script.py <rows> <columns>"
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    table = [[i + j for j in range(m)] for i in range(n)]

    print(generate_latex_table(table))


if __name__ == "__main__":
    main()
