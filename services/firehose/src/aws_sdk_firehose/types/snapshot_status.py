"""Generated from Smithy shape ``com.amazonaws.firehose#SnapshotStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

SnapshotStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "SUSPENDED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETE",
        "SUSPENDED",
    )
)


def serialize_aws_json_1_1(value: SnapshotStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnapshotStatus value: {data!r}")
    return cast(SnapshotStatus, data)
