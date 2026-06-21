"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneDriftStatus``."""

from typing import Literal, TypeAlias, cast

LandingZoneDriftStatus: TypeAlias = Literal[
    "DRIFTED",
    "IN_SYNC",
]


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneDriftStatus) -> str:
    return value


def deserialize_json(data: str) -> LandingZoneDriftStatus:
    return cast(LandingZoneDriftStatus, data)
