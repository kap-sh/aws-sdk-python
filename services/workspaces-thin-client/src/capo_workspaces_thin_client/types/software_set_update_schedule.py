"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#SoftwareSetUpdateSchedule``."""

from typing import Literal, TypeAlias, cast

SoftwareSetUpdateSchedule: TypeAlias = Literal[
    "USE_MAINTENANCE_WINDOW",
    "APPLY_IMMEDIATELY",
]


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareSetUpdateSchedule) -> str:
    return value


def deserialize_json(data: str) -> SoftwareSetUpdateSchedule:
    return cast(SoftwareSetUpdateSchedule, data)
