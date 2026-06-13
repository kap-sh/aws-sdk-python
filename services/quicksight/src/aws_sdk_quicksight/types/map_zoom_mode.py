"""Generated from Smithy shape ``com.amazonaws.quicksight#MapZoomMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

MapZoomMode: TypeAlias = Literal[
    "AUTO",
    "MANUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "MANUAL",
    )
)


def serialize_json(value: MapZoomMode) -> str:
    return value


def deserialize_json(data: str) -> MapZoomMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MapZoomMode value: {data!r}")
    return cast(MapZoomMode, data)
