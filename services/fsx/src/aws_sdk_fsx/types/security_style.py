"""Generated from Smithy shape ``com.amazonaws.fsx#SecurityStyle``."""

from typing import Literal, TypeAlias, cast

SecurityStyle: TypeAlias = Literal[
    "UNIX",
    "NTFS",
    "MIXED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityStyle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SecurityStyle:
    return cast(SecurityStyle, data)
