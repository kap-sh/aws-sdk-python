"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Ac3DynamicRangeCompressionProfile``."""

from typing import Literal, TypeAlias, cast

"""When you want to add Dolby dynamic range compression (DRC) signaling to your output stream, we recommend that you use the mode-specific settings instead of Dynamic range compression profile. The mode-specific settings are Dynamic range compression profile, line mode and Dynamic range compression profile, RF mode. Note that when you specify values for all three settings, MediaConvert ignores the value of this setting in favor of the mode-specific settings. If you do use this setting instead of the mode-specific settings, choose None to leave out DRC signaling. Keep the default Film standard to set the profile to Dolby's film standard profile for all operating modes."""
Ac3DynamicRangeCompressionProfile: TypeAlias = Literal[
    "FILM_STANDARD",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Ac3DynamicRangeCompressionProfile) -> str:
    return value


def deserialize_json(data: str) -> Ac3DynamicRangeCompressionProfile:
    return cast(Ac3DynamicRangeCompressionProfile, data)
