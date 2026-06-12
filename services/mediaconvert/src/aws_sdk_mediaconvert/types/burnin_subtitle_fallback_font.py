"""Generated from Smithy shape ``com.amazonaws.mediaconvert#BurninSubtitleFallbackFont``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the font that you want the service to use for your burn in captions when your input captions specify a font that MediaConvert doesn't support. When you set Fallback font to best match, or leave blank, MediaConvert uses a supported font that most closely matches the font that your input captions specify. When there are multiple unsupported fonts in your input captions, MediaConvert matches each font with the supported font that matches best. When you explicitly choose a replacement font, MediaConvert uses that font to replace all unsupported fonts from your input."""
BurninSubtitleFallbackFont: TypeAlias = Literal[
    "BEST_MATCH",
    "MONOSPACED_SANSSERIF",
    "MONOSPACED_SERIF",
    "PROPORTIONAL_SANSSERIF",
    "PROPORTIONAL_SERIF",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BEST_MATCH",
        "MONOSPACED_SANSSERIF",
        "MONOSPACED_SERIF",
        "PROPORTIONAL_SANSSERIF",
        "PROPORTIONAL_SERIF",
    )
)


def serialize_json(value: BurninSubtitleFallbackFont) -> str:
    return value


def deserialize_json(data: str) -> BurninSubtitleFallbackFont:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BurninSubtitleFallbackFont value: {data!r}"
        )
    return cast(BurninSubtitleFallbackFont, data)
