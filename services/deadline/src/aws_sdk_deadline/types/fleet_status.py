"""Generated from Smithy shape ``com.amazonaws.deadline#FleetStatus``."""

from typing import Literal, TypeAlias, cast

FleetStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATE_IN_PROGRESS",
    "UPDATE_IN_PROGRESS",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "SUSPENDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FleetStatus) -> str:
    return value


def deserialize_json(data: str) -> FleetStatus:
    return cast(FleetStatus, data)
