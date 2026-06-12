"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#HighlightColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

HighlightColor: TypeAlias = Literal[
    "Black",
    "Blue",
    "Red",
    "Green",
    "White",
    "Yellow",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Black",
        "Blue",
        "Red",
        "Green",
        "White",
        "Yellow",
    )
)


def serialize_json(value: HighlightColor) -> str:
    return value


def deserialize_json(data: str) -> HighlightColor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HighlightColor value: {data!r}")
    return cast(HighlightColor, data)
