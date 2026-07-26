"""Generated from Smithy shape ``com.amazonaws.connecthealth#Specialty``."""

from typing import Literal, TypeAlias, cast

Specialty: TypeAlias = Literal["PRIMARY_CARE",]


# --- restJson1 ser/de ---
def serialize_json(value: Specialty) -> str:
    return value


def deserialize_json(data: str) -> Specialty:
    return cast(Specialty, data)
