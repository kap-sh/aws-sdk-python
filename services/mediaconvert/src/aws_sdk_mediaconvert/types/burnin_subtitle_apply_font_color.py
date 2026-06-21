"""Generated from Smithy shape ``com.amazonaws.mediaconvert#BurninSubtitleApplyFontColor``."""

from typing import Literal, TypeAlias, cast

"""Ignore this setting unless Style passthrough is set to Enabled and Font color set to Black, Yellow, Red, Green, Blue, or Hex. Use Apply font color for additional font color controls. When you choose White text only, or leave blank, your font color setting only applies to white text in your input captions. For example, if your font color setting is Yellow, and your input captions have red and white text, your output captions will have red and yellow text. When you choose ALL_TEXT, your font color setting applies to all of your output captions text."""
BurninSubtitleApplyFontColor: TypeAlias = Literal[
    "WHITE_TEXT_ONLY",
    "ALL_TEXT",
]


# --- restJson1 ser/de ---
def serialize_json(value: BurninSubtitleApplyFontColor) -> str:
    return value


def deserialize_json(data: str) -> BurninSubtitleApplyFontColor:
    return cast(BurninSubtitleApplyFontColor, data)
