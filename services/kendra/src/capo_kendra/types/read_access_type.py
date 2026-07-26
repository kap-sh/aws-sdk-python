"""Generated from Smithy shape ``com.amazonaws.kendra#ReadAccessType``."""

from typing import Literal, TypeAlias, cast

ReadAccessType: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReadAccessType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReadAccessType:
    return cast(ReadAccessType, data)
