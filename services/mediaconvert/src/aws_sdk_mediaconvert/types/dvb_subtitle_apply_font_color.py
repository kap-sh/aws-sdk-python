"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DvbSubtitleApplyFontColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Ignore this setting unless Style Passthrough is set to Enabled and Font color set to Black, Yellow, Red, Green, Blue, or Hex. Use Apply font color for additional font color controls. When you choose White text only, or leave blank, your font color setting only applies to white text in your input captions. For example, if your font color setting is Yellow, and your input captions have red and white text, your output captions will have red and yellow text. When you choose ALL_TEXT, your font color setting applies to all of your output captions text."""
DvbSubtitleApplyFontColor: TypeAlias = Literal[
    "WHITE_TEXT_ONLY",
    "ALL_TEXT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WHITE_TEXT_ONLY",
        "ALL_TEXT",
    )
)


def serialize_json(value: DvbSubtitleApplyFontColor) -> str:
    return value


def deserialize_json(data: str) -> DvbSubtitleApplyFontColor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DvbSubtitleApplyFontColor value: {data!r}")
    return cast(DvbSubtitleApplyFontColor, data)
