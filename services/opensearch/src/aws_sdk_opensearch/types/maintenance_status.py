"""Generated from Smithy shape ``com.amazonaws.opensearch#MaintenanceStatus``."""

from typing import Literal, TypeAlias, cast

MaintenanceStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceStatus) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceStatus:
    return cast(MaintenanceStatus, data)
