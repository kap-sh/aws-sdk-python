"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisStatus``."""

from typing import Literal, TypeAlias, cast

EphemerisStatus: TypeAlias = Literal[
    "VALIDATING",
    "INVALID",
    "ERROR",
    "ENABLED",
    "DISABLED",
    "EXPIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisStatus) -> str:
    return value


def deserialize_json(data: str) -> EphemerisStatus:
    return cast(EphemerisStatus, data)
