"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialLayerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

GeospatialLayerType: TypeAlias = Literal[
    "POINT",
    "LINE",
    "POLYGON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "POINT",
        "LINE",
        "POLYGON",
    )
)


def serialize_json(value: GeospatialLayerType) -> str:
    return value


def deserialize_json(data: str) -> GeospatialLayerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GeospatialLayerType value: {data!r}")
    return cast(GeospatialLayerType, data)
