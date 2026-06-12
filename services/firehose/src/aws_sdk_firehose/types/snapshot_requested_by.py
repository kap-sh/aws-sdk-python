"""Generated from Smithy shape ``com.amazonaws.firehose#SnapshotRequestedBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

SnapshotRequestedBy: TypeAlias = Literal[
    "USER",
    "FIREHOSE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "FIREHOSE",
    )
)


def serialize_aws_json_1_1(value: SnapshotRequestedBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotRequestedBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnapshotRequestedBy value: {data!r}")
    return cast(SnapshotRequestedBy, data)
