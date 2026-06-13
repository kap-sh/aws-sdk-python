"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialMapNavigation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

GeospatialMapNavigation: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: GeospatialMapNavigation) -> str:
    return value


def deserialize_json(data: str) -> GeospatialMapNavigation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GeospatialMapNavigation value: {data!r}")
    return cast(GeospatialMapNavigation, data)
