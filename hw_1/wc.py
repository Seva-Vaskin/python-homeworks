import sys
from pathlib import Path
from collections import deque


def wc(source):
    data = source.read()
    lines_count = data.count('\n')
    words_count = len(data.split())
    bytes_count = len(data.encode('utf-8'))
    return lines_count, words_count, bytes_count


def get_width(elements):
    return max(map(lambda x: len(str(x)), elements))


def print_stat(lines_count, words_count, bytes_count, width=None, name=None):
    if width is None:
        width = get_width((lines_count, words_count, bytes_count))

    format_spec = f"{{:>{width}}} {{:>{width}}} {{:>{width}}}"
    if name:
        print(format_spec.format(lines_count, words_count, bytes_count), name)
    else:
        print(format_spec.format(lines_count, words_count, bytes_count))


def main():
    if len(sys.argv) > 1:
        stat = []
        for i in range(1, len(sys.argv)):
            file_path = Path(sys.argv[i])
            if not file_path.exists():
                print(f"{sys.argv[0]}: '{file_path}': No such file or directory",
                      file=sys.stderr)
                continue
            if file_path.is_dir():
                print(f"{sys.argv[0]}: {file_path}: Is a directory", file=sys.stderr)
                print_stat(0, 0, 0, None, file_path)
                continue
            if not file_path.is_file():
                print(f"{sys.argv[0]}: {file_path}: Is not a file", file=sys.stderr)
                continue

            with file_path.open('r') as f:
                stat.append((*wc(f), file_path))

        total_lines, total_words, total_bytes = 0, 0, 0
        for lines_count, words_count, bytes_count, _ in stat:
            total_lines += lines_count
            total_words += words_count
            total_bytes += bytes_count

        width = get_width((total_lines, total_words, total_bytes))
        for lines_count, words_count, bytes_count, file_path in stat:
            print_stat(lines_count, words_count, bytes_count, width, file_path)
        if len(sys.argv) > 2:
            print_stat(total_lines, total_words, total_bytes, width, 'total')
    else:
        print_stat(*wc(sys.stdin))


if __name__ == "__main__":
    main()
