"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisType``."""

from typing import Literal, TypeAlias, cast

EphemerisType: TypeAlias = Literal[
    "TLE",
    "OEM",
    "AZ_EL",
    "SERVICE_MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisType) -> str:
    return value


def deserialize_json(data: str) -> EphemerisType:
    return cast(EphemerisType, data)
