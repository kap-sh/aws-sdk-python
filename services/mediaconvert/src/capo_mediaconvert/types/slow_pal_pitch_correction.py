"""Generated from Smithy shape ``com.amazonaws.mediaconvert#SlowPalPitchCorrection``."""

from typing import Literal, TypeAlias, cast

"""Use Slow PAL pitch correction to compensate for audio pitch changes during slow PAL frame rate conversion. This setting only applies when Slow PAL is enabled in your output video codec settings. To automatically apply audio pitch correction: Choose Enabled. MediaConvert automatically applies a pitch correction to your output to match the original content's audio pitch. To not apply audio pitch correction: Keep the default value, Disabled."""
SlowPalPitchCorrection: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SlowPalPitchCorrection) -> str:
    return value


def deserialize_json(data: str) -> SlowPalPitchCorrection:
    return cast(SlowPalPitchCorrection, data)
