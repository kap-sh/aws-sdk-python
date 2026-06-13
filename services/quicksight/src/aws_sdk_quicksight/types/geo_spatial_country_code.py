"""Generated from Smithy shape ``com.amazonaws.quicksight#GeoSpatialCountryCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

GeoSpatialCountryCode: TypeAlias = Literal["US",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("US",))


def serialize_json(value: GeoSpatialCountryCode) -> str:
    return value


def deserialize_json(data: str) -> GeoSpatialCountryCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GeoSpatialCountryCode value: {data!r}")
    return cast(GeoSpatialCountryCode, data)
