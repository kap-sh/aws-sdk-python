"""Generated from Smithy shape ``com.amazonaws.medialive#MaintenanceDay``."""

from typing import Literal, TypeAlias, cast

"""The currently selected maintenance day."""
MaintenanceDay: TypeAlias = Literal[
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceDay) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceDay:
    return cast(MaintenanceDay, data)
