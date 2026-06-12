"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VerticalTilePosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

VerticalTilePosition: TypeAlias = Literal[
    "Left",
    "Right",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Left",
        "Right",
    )
)


def serialize_json(value: VerticalTilePosition) -> str:
    return value


def deserialize_json(data: str) -> VerticalTilePosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VerticalTilePosition value: {data!r}")
    return cast(VerticalTilePosition, data)
