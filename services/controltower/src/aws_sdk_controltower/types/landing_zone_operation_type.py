"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneOperationType``."""

from typing import Literal, TypeAlias, cast

LandingZoneOperationType: TypeAlias = Literal[
    "DELETE",
    "CREATE",
    "UPDATE",
    "RESET",
]


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneOperationType) -> str:
    return value


def deserialize_json(data: str) -> LandingZoneOperationType:
    return cast(LandingZoneOperationType, data)
