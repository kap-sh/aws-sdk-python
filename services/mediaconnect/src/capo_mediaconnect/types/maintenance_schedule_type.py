"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MaintenanceScheduleType``."""

from typing import Literal, TypeAlias, cast

MaintenanceScheduleType: TypeAlias = Literal["WINDOW",]


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceScheduleType) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceScheduleType:
    return cast(MaintenanceScheduleType, data)
