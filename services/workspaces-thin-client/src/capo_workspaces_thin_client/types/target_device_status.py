"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#TargetDeviceStatus``."""

from typing import Literal, TypeAlias, cast

TargetDeviceStatus: TypeAlias = Literal[
    "DEREGISTERED",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetDeviceStatus) -> str:
    return value


def deserialize_json(data: str) -> TargetDeviceStatus:
    return cast(TargetDeviceStatus, data)
