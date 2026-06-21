"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AdvancedInputFilterSharpen``."""

from typing import Literal, TypeAlias, cast

"""Optionally specify the amount of sharpening to apply when you use the Advanced input filter. Sharpening adds contrast to the edges of your video content and can reduce softness. To apply no sharpening: Keep the default value, Off. To apply a minimal amount of sharpening choose Low, or for the maximum choose High."""
AdvancedInputFilterSharpen: TypeAlias = Literal[
    "OFF",
    "LOW",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedInputFilterSharpen) -> str:
    return value


def deserialize_json(data: str) -> AdvancedInputFilterSharpen:
    return cast(AdvancedInputFilterSharpen, data)
