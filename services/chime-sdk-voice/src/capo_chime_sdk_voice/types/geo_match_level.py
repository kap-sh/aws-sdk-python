"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GeoMatchLevel``."""

from typing import Literal, TypeAlias, cast

GeoMatchLevel: TypeAlias = Literal[
    "Country",
    "AreaCode",
]


# --- restJson1 ser/de ---
def serialize_json(value: GeoMatchLevel) -> str:
    return value


def deserialize_json(data: str) -> GeoMatchLevel:
    return cast(GeoMatchLevel, data)
