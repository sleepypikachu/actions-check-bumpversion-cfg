import configparser
import sys
from typing import Iterable, List


def parse_version(version_string: str) -> List[int]:
    return [int(x) for x in version_string.split(".")]


def new_greater_than_current(
    current_version_parts: Iterable[int], new_version_parts: Iterable[int]
):
    for current_part, new_part in zip(current_version_parts, new_version_parts):
        if new_part > current_part:
            return True
        if new_part < current_part:
            return False
    return False


def format_bumpversion_github_action_error(error_message: str) -> str:
    return f"::error file=.bumpversion.cfg::{error_message}"


if __name__ == "__main__":
    parser = configparser.ConfigParser()
    parser.read(".bumpversion.cfg")

    try:
        current_version = parser["bumpversion"]["current_version"]
        new_version = parser["bumpversion"]["new_version"]
    except KeyError as e:
        print(format_bumpversion_github_action_error(f"Config does not contain {e}"))
        sys.exit(10)

    try:
        current_parts = parse_version(current_version)
        new_parts = parse_version(new_version)
    except ValueError as e:
        print(format_bumpversion_github_action_error(str(e)))
        sys.exit(11)

    if len(current_parts) != len(new_parts):
        print(
            format_bumpversion_github_action_error(
                f"Different number of version parts: {current_version} vs {new_version}"
            )
        )
        sys.exit(12)

    if not new_greater_than_current(current_parts, new_parts):
        print(
            format_bumpversion_github_action_error(
                f"New version {new_version} <= current version {current_version}"
            )
        )
        sys.exit(13)
