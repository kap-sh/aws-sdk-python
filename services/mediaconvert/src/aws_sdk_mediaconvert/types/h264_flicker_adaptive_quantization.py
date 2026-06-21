"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264FlickerAdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

"""Only use this setting when you change the default value, AUTO, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264FlickerAdaptiveQuantization is Disabled. Change this value to Enabled to reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. To manually enable or disable H264FlickerAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO."""
H264FlickerAdaptiveQuantization: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264FlickerAdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> H264FlickerAdaptiveQuantization:
    return cast(H264FlickerAdaptiveQuantization, data)
