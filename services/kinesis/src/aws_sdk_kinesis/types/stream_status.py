"""Generated from Smithy shape ``com.amazonaws.kinesis#StreamStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis.errors import DeserializationError

StreamStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "ACTIVE",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "DELETING",
        "ACTIVE",
        "UPDATING",
    )
)


def serialize_aws_json_1_1(value: StreamStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StreamStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamStatus value: {data!r}")
    return cast(StreamStatus, data)
