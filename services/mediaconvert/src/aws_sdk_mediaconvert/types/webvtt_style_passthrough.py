"""Generated from Smithy shape ``com.amazonaws.mediaconvert#WebvttStylePassthrough``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify how MediaConvert writes style information in your output WebVTT captions. To use the available style, color, and position information from your input captions: Choose Enabled. MediaConvert uses default settings when style and position information is missing from your input captions. To recreate the input captions exactly: Choose Strict. MediaConvert automatically applies timing adjustments, including adjustments for frame rate conversion, ad avails, and input clipping. Your input captions format must be WebVTT. To ignore the style and position information from your input captions and use simplified output captions: Keep the default value, Disabled. Or leave blank. To use the available style, color, and position information from your input captions, while merging cues with identical time ranges: Choose merge. This setting can help prevent positioning overlaps for certain players that expect a single single cue for any given time range."""
WebvttStylePassthrough: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "STRICT",
    "MERGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "STRICT",
        "MERGE",
    )
)


def serialize_json(value: WebvttStylePassthrough) -> str:
    return value


def deserialize_json(data: str) -> WebvttStylePassthrough:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WebvttStylePassthrough value: {data!r}")
    return cast(WebvttStylePassthrough, data)
