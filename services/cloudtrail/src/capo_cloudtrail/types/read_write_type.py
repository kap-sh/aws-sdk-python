"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ReadWriteType``."""

from typing import Literal, TypeAlias, cast

ReadWriteType: TypeAlias = Literal[
    "ReadOnly",
    "WriteOnly",
    "All",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReadWriteType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReadWriteType:
    return cast(ReadWriteType, data)
