#!/usr/bin/env python3
import subprocess


def run_command(cmd):
    result = subprocess.run(cmd, check=False, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return result.stdout.decode()


def main():
    result = run_command('dir')
    print(result)


if __name__ == '__main__':
    main()
