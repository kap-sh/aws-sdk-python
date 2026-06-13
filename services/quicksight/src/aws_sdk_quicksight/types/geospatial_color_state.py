"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialColorState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

GeospatialColorState: TypeAlias = Literal[
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


def serialize_json(value: GeospatialColorState) -> str:
    return value


def deserialize_json(data: str) -> GeospatialColorState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GeospatialColorState value: {data!r}")
    return cast(GeospatialColorState, data)
