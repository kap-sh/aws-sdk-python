"""Generated from Smithy shape ``com.amazonaws.mediaconvert#SrtStylePassthrough``."""

from typing import Literal, TypeAlias, cast

"""Set Style passthrough to ENABLED to use the available style, color, and position information from your input captions. MediaConvert uses default settings for any missing style and position information in your input captions. Set Style passthrough to DISABLED, or leave blank, to ignore the style and position information from your input captions and use simplified output captions."""
SrtStylePassthrough: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SrtStylePassthrough) -> str:
    return value


def deserialize_json(data: str) -> SrtStylePassthrough:
    return cast(SrtStylePassthrough, data)
