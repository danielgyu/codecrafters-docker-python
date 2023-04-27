import os
import subprocess
import sys


def main():
    command = sys.argv[3]
    args = sys.argv[4:]

    completed_process = subprocess.run(
        [command, *args],
        capture_output=True,
    )
    os.write(sys.stdout.fileno(), completed_process.stdout)
    os.write(sys.stderr.fileno(), completed_process.stderr)

    exit(completed_process.returncode)

if __name__ == "__main__":
    main()
