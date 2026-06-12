"""Generated from Smithy shape ``com.amazonaws.lightsail#DiskSnapshotState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

DiskSnapshotState: TypeAlias = Literal[
    "pending",
    "completed",
    "error",
    "unknown",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "completed",
        "error",
        "unknown",
    )
)


def serialize_aws_json_1_1(value: DiskSnapshotState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DiskSnapshotState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DiskSnapshotState value: {data!r}")
    return cast(DiskSnapshotState, data)
