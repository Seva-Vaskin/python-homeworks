import sys
from pathlib import Path

line_number = 1


def print_numbered_lines(source):
    global line_number
    for line in source:
        print(f"{line_number:>5}\t{line}", end='')
        line_number += 1


def main():
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            file_path = Path(sys.argv[i])
            if not file_path.exists():
                print(f"{sys.argv[0]}: {file_path}: No such file or directory", file=sys.stderr)
            elif file_path.is_dir():
                print(f"{sys.argv[0]}: {file_path}: Is a directory", file=sys.stderr)
            elif not file_path.is_file():
                print(f"{sys.argv[0]}: {file_path}: Is not a file", file=sys.stderr)
            else:
                with file_path.open('r') as f:
                    print_numbered_lines(f)
    else:
        print_numbered_lines(sys.stdin)


if __name__ == "__main__":
    main()
