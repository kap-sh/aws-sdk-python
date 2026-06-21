"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcAdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

"""Keep the default value, Auto, for this setting to have MediaConvert automatically apply the best types of quantization for your video content. When you want to apply your quantization settings manually, you must set Adaptive quantization to a value other than Auto. Use this setting to specify the strength of any adaptive quantization filters that you enable. If you don't want MediaConvert to do any adaptive quantization in this transcode, set Adaptive quantization to Off. Related settings: The value that you choose here applies to the following settings: Flicker adaptive quantization (flickerAdaptiveQuantization), Spatial adaptive quantization, and Temporal adaptive quantization."""
XavcAdaptiveQuantization: TypeAlias = Literal[
    "OFF",
    "AUTO",
    "LOW",
    "MEDIUM",
    "HIGH",
    "HIGHER",
    "MAX",
]


# --- restJson1 ser/de ---
def serialize_json(value: XavcAdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> XavcAdaptiveQuantization:
    return cast(XavcAdaptiveQuantization, data)
