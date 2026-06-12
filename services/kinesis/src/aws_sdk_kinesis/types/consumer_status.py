"""Generated from Smithy shape ``com.amazonaws.kinesis#ConsumerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis.errors import DeserializationError

ConsumerStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "ACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "DELETING",
        "ACTIVE",
    )
)


def serialize_aws_json_1_1(value: ConsumerStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConsumerStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConsumerStatus value: {data!r}")
    return cast(ConsumerStatus, data)
