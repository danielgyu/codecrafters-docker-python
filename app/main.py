#import subprocess
import sys


def main():
    _ = sys.argv[3]

    docker_command = sys.argv[4]
    docker_args = sys.argv[5:]

    match docker_command:
        case "echo":
            print(docker_args[0])
        case "echo_stderr":
            print(docker_args[0])
            print("what???")
        case _:
            raise NotImplementedError()

    # completed_process = subprocess.run([command, *args], capture_output=True)
    # print(completed_process.stdout.decode("utf-8"))


if __name__ == "__main__":
    main()
