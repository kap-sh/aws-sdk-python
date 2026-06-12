"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#HorizontalTilePosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

HorizontalTilePosition: TypeAlias = Literal[
    "Top",
    "Bottom",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Top",
        "Bottom",
    )
)


def serialize_json(value: HorizontalTilePosition) -> str:
    return value


def deserialize_json(data: str) -> HorizontalTilePosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HorizontalTilePosition value: {data!r}")
    return cast(HorizontalTilePosition, data)
