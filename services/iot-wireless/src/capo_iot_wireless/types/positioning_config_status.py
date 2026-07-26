"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositioningConfigStatus``."""

from typing import Literal, TypeAlias, cast

PositioningConfigStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: PositioningConfigStatus) -> str:
    return value


def deserialize_json(data: str) -> PositioningConfigStatus:
    return cast(PositioningConfigStatus, data)
