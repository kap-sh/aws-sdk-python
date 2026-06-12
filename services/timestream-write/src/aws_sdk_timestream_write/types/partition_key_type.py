"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#PartitionKeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_write.errors import DeserializationError

PartitionKeyType: TypeAlias = Literal[
    "DIMENSION",
    "MEASURE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIMENSION",
        "MEASURE",
    )
)


def serialize_aws_json_1_0(value: PartitionKeyType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PartitionKeyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PartitionKeyType value: {data!r}")
    return cast(PartitionKeyType, data)
