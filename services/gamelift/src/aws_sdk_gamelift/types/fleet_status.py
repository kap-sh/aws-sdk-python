"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

FleetStatus: TypeAlias = Literal[
    "NEW",
    "DOWNLOADING",
    "VALIDATING",
    "BUILDING",
    "ACTIVATING",
    "ACTIVE",
    "DELETING",
    "ERROR",
    "TERMINATED",
    "NOT_FOUND",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEW",
        "DOWNLOADING",
        "VALIDATING",
        "BUILDING",
        "ACTIVATING",
        "ACTIVE",
        "DELETING",
        "ERROR",
        "TERMINATED",
        "NOT_FOUND",
    )
)


def serialize_aws_json_1_1(value: FleetStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetStatus value: {data!r}")
    return cast(FleetStatus, data)
