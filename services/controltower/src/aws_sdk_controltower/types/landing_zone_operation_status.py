"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneOperationStatus``."""

from typing import Literal, TypeAlias, cast

LandingZoneOperationStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneOperationStatus) -> str:
    return value


def deserialize_json(data: str) -> LandingZoneOperationStatus:
    return cast(LandingZoneOperationStatus, data)
