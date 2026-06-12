"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#Compression``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

Compression: TypeAlias = Literal[
    "OFF",
    "SNAPPY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "SNAPPY",
    )
)


def serialize_aws_json_1_0(value: Compression) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Compression:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Compression value: {data!r}")
    return cast(Compression, data)
