"""Generated from Smithy shape ``com.amazonaws.quicksight#GeoSpatialCountryCode``."""

from typing import Literal, TypeAlias, cast

GeoSpatialCountryCode: TypeAlias = Literal["US",]


# --- restJson1 ser/de ---
def serialize_json(value: GeoSpatialCountryCode) -> str:
    return value


def deserialize_json(data: str) -> GeoSpatialCountryCode:
    return cast(GeoSpatialCountryCode, data)
