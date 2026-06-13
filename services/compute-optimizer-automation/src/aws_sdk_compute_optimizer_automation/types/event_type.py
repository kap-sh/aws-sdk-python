"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#EventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

"""Event type enumeration"""
EventType: TypeAlias = Literal[
    "SnapshotAndDeleteUnattachedEbsVolume",
    "UpgradeEbsVolumeType",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SnapshotAndDeleteUnattachedEbsVolume",
        "UpgradeEbsVolumeType",
    )
)


def serialize_aws_json_1_0(value: EventType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventType value: {data!r}")
    return cast(EventType, data)
