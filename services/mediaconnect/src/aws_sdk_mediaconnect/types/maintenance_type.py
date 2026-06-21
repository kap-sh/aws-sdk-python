"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MaintenanceType``."""

from typing import Literal, TypeAlias, cast

MaintenanceType: TypeAlias = Literal[
    "PREFERRED_DAY_TIME",
    "DEFAULT",
]


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceType) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceType:
    return cast(MaintenanceType, data)
