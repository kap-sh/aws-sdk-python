"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceSnapshotState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

InstanceSnapshotState: TypeAlias = Literal[
    "pending",
    "error",
    "available",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "error",
        "available",
    )
)


def serialize_aws_json_1_1(value: InstanceSnapshotState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceSnapshotState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceSnapshotState value: {data!r}")
    return cast(InstanceSnapshotState, data)
