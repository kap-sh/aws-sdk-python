"""Generated from Smithy shape ``com.amazonaws.glue#PartitionIndexStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

PartitionIndexStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: PartitionIndexStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PartitionIndexStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PartitionIndexStatus value: {data!r}")
    return cast(PartitionIndexStatus, data)
