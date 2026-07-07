"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioPitchCorrectionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.slow_pal_pitch_correction


class AudioPitchCorrectionSettings(TypedDict, closed=True):
    slow_pal_pitch_correction: NotRequired[
        "aws_sdk_mediaconvert.types.slow_pal_pitch_correction.SlowPalPitchCorrection"
    ]
    """Use Slow PAL pitch correction to compensate for audio pitch changes during slow PAL frame rate conversion. This setting only applies when Slow PAL is enabled in your output video codec settings. To automatically apply audio pitch correction: Choose Enabled. MediaConvert automatically applies a pitch correction to your output to match the original content's audio pitch. To not apply audio pitch correction: Keep the default value, Disabled."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioPitchCorrectionSettings) -> dict:
    out: dict = {}
    if "slow_pal_pitch_correction" in value:
        import aws_sdk_mediaconvert.types.slow_pal_pitch_correction

        out["slowPalPitchCorrection"] = (
            aws_sdk_mediaconvert.types.slow_pal_pitch_correction.serialize_json(
                value["slow_pal_pitch_correction"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioPitchCorrectionSettings:
    out: AudioPitchCorrectionSettings = {}  # type: ignore[typeddict-item]
    if "slowPalPitchCorrection" in data:
        import aws_sdk_mediaconvert.types.slow_pal_pitch_correction

        out["slow_pal_pitch_correction"] = (
            aws_sdk_mediaconvert.types.slow_pal_pitch_correction.deserialize_json(
                data["slowPalPitchCorrection"]
            )
        )
    return out
