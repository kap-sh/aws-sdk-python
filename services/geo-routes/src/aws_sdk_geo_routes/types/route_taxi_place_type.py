"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiPlaceType``."""

from typing import Literal, TypeAlias, cast

RouteTaxiPlaceType: TypeAlias = Literal[
    "AccessPoint",
    "Station",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiPlaceType) -> str:
    return value


def deserialize_json(data: str) -> RouteTaxiPlaceType:
    return cast(RouteTaxiPlaceType, data)
