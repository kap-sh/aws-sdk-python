"""Generated from Smithy shape ``com.amazonaws.deadline#FleetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

FleetStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATE_IN_PROGRESS",
    "UPDATE_IN_PROGRESS",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "SUSPENDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CREATE_IN_PROGRESS",
        "UPDATE_IN_PROGRESS",
        "CREATE_FAILED",
        "UPDATE_FAILED",
        "SUSPENDED",
    )
)


def serialize_json(value: FleetStatus) -> str:
    return value


def deserialize_json(data: str) -> FleetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetStatus value: {data!r}")
    return cast(FleetStatus, data)
