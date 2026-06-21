"""Generated from Smithy shape ``com.amazonaws.quicksight#GeoSpatialDataRole``."""

from typing import Literal, TypeAlias, cast

GeoSpatialDataRole: TypeAlias = Literal[
    "COUNTRY",
    "STATE",
    "COUNTY",
    "CITY",
    "POSTCODE",
    "LONGITUDE",
    "LATITUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GeoSpatialDataRole) -> str:
    return value


def deserialize_json(data: str) -> GeoSpatialDataRole:
    return cast(GeoSpatialDataRole, data)
