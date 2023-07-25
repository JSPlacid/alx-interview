import sys
from collections import defaultdict

def print_metrics(total_size, status_codes):
    print(f"Total file size: File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def main():
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()
            if len(parts) != 7:
                continue

            ip, _, _, method, path, _, status_code, file_size = parts

            if method != 'GET' or not path.startswith('/projects/'):
                continue

            try:
                file_size = int(file_size)
            except ValueError:
                continue

            total_size += file_size
            status_codes[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)

if __name__ == "__main__":
    main()

