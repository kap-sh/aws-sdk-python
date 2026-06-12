"""Generated from Smithy shape ``com.amazonaws.frauddetector#DataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

DataType: TypeAlias = Literal[
    "STRING",
    "INTEGER",
    "FLOAT",
    "BOOLEAN",
    "DATETIME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "INTEGER",
        "FLOAT",
        "BOOLEAN",
        "DATETIME",
    )
)


def serialize_aws_json_1_1(value: DataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataType value: {data!r}")
    return cast(DataType, data)
