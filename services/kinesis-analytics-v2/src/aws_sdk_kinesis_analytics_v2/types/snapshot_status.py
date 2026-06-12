"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

SnapshotStatus: TypeAlias = Literal[
    "CREATING",
    "READY",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "READY",
        "DELETING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: SnapshotStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnapshotStatus value: {data!r}")
    return cast(SnapshotStatus, data)
