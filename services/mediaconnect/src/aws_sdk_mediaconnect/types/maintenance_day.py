"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MaintenanceDay``."""

from typing import Literal, TypeAlias, cast

MaintenanceDay: TypeAlias = Literal[
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceDay) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceDay:
    return cast(MaintenanceDay, data)
