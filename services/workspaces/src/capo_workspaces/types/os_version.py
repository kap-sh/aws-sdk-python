"""Generated from Smithy shape ``com.amazonaws.workspaces#OSVersion``."""

from typing import Literal, TypeAlias, cast

OSVersion: TypeAlias = Literal[
    "Windows_10",
    "Windows_11",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OSVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OSVersion:
    return cast(OSVersion, data)
