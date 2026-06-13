"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#ClusterStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_influxdb.errors import DeserializationError

ClusterStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "AVAILABLE",
    "FAILED",
    "DELETED",
    "MAINTENANCE",
    "UPDATING_INSTANCE_TYPE",
    "REBOOTING",
    "REBOOT_FAILED",
    "PARTIALLY_AVAILABLE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "DELETING",
        "AVAILABLE",
        "FAILED",
        "DELETED",
        "MAINTENANCE",
        "UPDATING_INSTANCE_TYPE",
        "REBOOTING",
        "REBOOT_FAILED",
        "PARTIALLY_AVAILABLE",
    )
)


def serialize_aws_json_1_0(value: ClusterStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ClusterStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterStatus value: {data!r}")
    return cast(ClusterStatus, data)
