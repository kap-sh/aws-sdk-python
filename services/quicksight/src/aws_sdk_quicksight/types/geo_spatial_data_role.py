"""Generated from Smithy shape ``com.amazonaws.quicksight#GeoSpatialDataRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "COUNTRY",
        "STATE",
        "COUNTY",
        "CITY",
        "POSTCODE",
        "LONGITUDE",
        "LATITUDE",
    )
)


def serialize_json(value: GeoSpatialDataRole) -> str:
    return value


def deserialize_json(data: str) -> GeoSpatialDataRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GeoSpatialDataRole value: {data!r}")
    return cast(GeoSpatialDataRole, data)
