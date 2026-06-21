"""Generated from Smithy shape ``com.amazonaws.frauddetector#DataType``."""

from typing import Literal, TypeAlias, cast

DataType: TypeAlias = Literal[
    "STRING",
    "INTEGER",
    "FLOAT",
    "BOOLEAN",
    "DATETIME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataType:
    return cast(DataType, data)
