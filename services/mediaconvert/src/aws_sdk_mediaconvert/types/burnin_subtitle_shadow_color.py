"""Generated from Smithy shape ``com.amazonaws.mediaconvert#BurninSubtitleShadowColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the color of the shadow cast by the captions. Leave Shadow color blank and set Style passthrough to enabled to use the shadow color data from your input captions, if present."""
BurninSubtitleShadowColor: TypeAlias = Literal[
    "NONE",
    "BLACK",
    "WHITE",
    "AUTO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "BLACK",
        "WHITE",
        "AUTO",
    )
)


def serialize_json(value: BurninSubtitleShadowColor) -> str:
    return value


def deserialize_json(data: str) -> BurninSubtitleShadowColor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BurninSubtitleShadowColor value: {data!r}")
    return cast(BurninSubtitleShadowColor, data)
