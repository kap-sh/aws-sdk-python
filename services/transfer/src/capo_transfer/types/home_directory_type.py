"""Generated from Smithy shape ``com.amazonaws.transfer#HomeDirectoryType``."""

from typing import Literal, TypeAlias, cast

HomeDirectoryType: TypeAlias = Literal[
    "PATH",
    "LOGICAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HomeDirectoryType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HomeDirectoryType:
    return cast(HomeDirectoryType, data)
