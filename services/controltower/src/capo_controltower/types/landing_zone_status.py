"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneStatus``."""

from typing import Literal, TypeAlias, cast

LandingZoneStatus: TypeAlias = Literal[
    "ACTIVE",
    "PROCESSING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneStatus) -> str:
    return value


def deserialize_json(data: str) -> LandingZoneStatus:
    return cast(LandingZoneStatus, data)
