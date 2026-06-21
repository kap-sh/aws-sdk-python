"""Generated from Smithy shape ``com.amazonaws.directoryservice#OSVersion``."""

from typing import Literal, TypeAlias, cast

OSVersion: TypeAlias = Literal[
    "SERVER_2012",
    "SERVER_2019",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OSVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OSVersion:
    return cast(OSVersion, data)
