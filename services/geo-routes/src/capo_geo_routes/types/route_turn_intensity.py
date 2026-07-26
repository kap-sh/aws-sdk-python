"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTurnIntensity``."""

from typing import Literal, TypeAlias, cast

RouteTurnIntensity: TypeAlias = Literal[
    "Sharp",
    "Slight",
    "Typical",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTurnIntensity) -> str:
    return value


def deserialize_json(data: str) -> RouteTurnIntensity:
    return cast(RouteTurnIntensity, data)
