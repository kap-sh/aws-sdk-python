"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#DeviceStatus``."""

from typing import Literal, TypeAlias, cast

DeviceStatus: TypeAlias = Literal[
    "REGISTERED",
    "DEREGISTERING",
    "DEREGISTERED",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceStatus) -> str:
    return value


def deserialize_json(data: str) -> DeviceStatus:
    return cast(DeviceStatus, data)
