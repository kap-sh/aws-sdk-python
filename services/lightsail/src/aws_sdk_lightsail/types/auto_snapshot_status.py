"""Generated from Smithy shape ``com.amazonaws.lightsail#AutoSnapshotStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

AutoSnapshotStatus: TypeAlias = Literal[
    "Success",
    "Failed",
    "InProgress",
    "NotFound",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Success",
        "Failed",
        "InProgress",
        "NotFound",
    )
)


def serialize_aws_json_1_1(value: AutoSnapshotStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoSnapshotStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoSnapshotStatus value: {data!r}")
    return cast(AutoSnapshotStatus, data)
