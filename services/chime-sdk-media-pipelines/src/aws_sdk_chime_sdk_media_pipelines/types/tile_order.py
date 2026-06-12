"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#TileOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

TileOrder: TypeAlias = Literal[
    "JoinSequence",
    "SpeakerSequence",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JoinSequence",
        "SpeakerSequence",
    )
)


def serialize_json(value: TileOrder) -> str:
    return value


def deserialize_json(data: str) -> TileOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TileOrder value: {data!r}")
    return cast(TileOrder, data)
