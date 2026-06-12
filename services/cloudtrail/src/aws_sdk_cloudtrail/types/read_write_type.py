"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ReadWriteType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

ReadWriteType: TypeAlias = Literal[
    "ReadOnly",
    "WriteOnly",
    "All",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ReadOnly",
        "WriteOnly",
        "All",
    )
)


def serialize_aws_json_1_1(value: ReadWriteType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReadWriteType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReadWriteType value: {data!r}")
    return cast(ReadWriteType, data)
