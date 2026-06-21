"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#MaintenanceWindowType``."""

from typing import Literal, TypeAlias, cast

MaintenanceWindowType: TypeAlias = Literal[
    "SYSTEM",
    "CUSTOM",
]


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceWindowType) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceWindowType:
    return cast(MaintenanceWindowType, data)
