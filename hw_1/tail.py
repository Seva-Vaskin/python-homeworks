import sys
from pathlib import Path
from collections import deque


def tail(source, lines):
    last_lines = deque(source, maxlen=lines)
    print(*last_lines, sep='', end='')


def main():
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            file_path = Path(sys.argv[i])
            if not file_path.exists():
                print(f"{sys.argv[0]}: cannot open '{file_path}' for reading: No such file or directory",
                      file=sys.stderr)
                continue
            if file_path.is_dir():
                print(f"{sys.argv[0]}: error reading {file_path}: Is a directory", file=sys.stderr)
                continue
            if not file_path.is_file():
                print(f"{sys.argv[0]}: {file_path}: Is not a file", file=sys.stderr)
                continue

            if i > 1:
                print()
            if len(sys.argv) > 2:
                print(f"==> {file_path} <==")
            with file_path.open('r') as f:
                tail(f, 10)
    else:
        tail(sys.stdin, 17)


if __name__ == "__main__":
    main()
