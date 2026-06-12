"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DvbSubtitleShadowColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the color of the shadow cast by the captions. Leave Shadow color blank and set Style passthrough to enabled to use the shadow color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical."""
DvbSubtitleShadowColor: TypeAlias = Literal[
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


def serialize_json(value: DvbSubtitleShadowColor) -> str:
    return value


def deserialize_json(data: str) -> DvbSubtitleShadowColor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DvbSubtitleShadowColor value: {data!r}")
    return cast(DvbSubtitleShadowColor, data)
