"""Generated from Smithy shape ``com.amazonaws.groundstation#MaintenanceType``."""

from typing import Literal, TypeAlias, cast

MaintenanceType: TypeAlias = Literal[
    "PLANNED",
    "UNPLANNED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceType) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceType:
    return cast(MaintenanceType, data)
