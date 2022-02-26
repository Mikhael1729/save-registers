import sys
import os

from io import TextIOWrapper
from typing import List

if len(sys.argv) == 1:
  print("No register passed")

registers = sys.argv[1:]
lines: List[str] = []


def main():
  total_recorded = len(registers)
  with open("results_register.txt", "a+") as file:
    for register in registers:
      if register_exists(file, register):
        total_recorded -= 1
        print(f"Register \"{register}\" exists (not recorded)")

        continue

      file.write(register + "\n")

  if total_recorded > 0:
    print(f"{total_recorded} result{'s' if total_recorded > 1 else ''} have been recorded")


def register_exists(file: TextIOWrapper, register: str) -> bool:
  file.seek(0)
  lines = file.readlines()

  return register + "\n" in lines


if __name__ == "__main__":
  main()
