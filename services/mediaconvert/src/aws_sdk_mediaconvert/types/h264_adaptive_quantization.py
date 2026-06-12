"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264AdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Keep the default value, Auto, for this setting to have MediaConvert automatically apply the best types of quantization for your video content. When you want to apply your quantization settings manually, you must set H264AdaptiveQuantization to a value other than Auto. Use this setting to specify the strength of any adaptive quantization filters that you enable. If you don't want MediaConvert to do any adaptive quantization in this transcode, set Adaptive quantization to Off. Related settings: The value that you choose here applies to the following settings: H264FlickerAdaptiveQuantization, H264SpatialAdaptiveQuantization, and H264TemporalAdaptiveQuantization."""
H264AdaptiveQuantization: TypeAlias = Literal[
    "OFF",
    "AUTO",
    "LOW",
    "MEDIUM",
    "HIGH",
    "HIGHER",
    "MAX",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "AUTO",
        "LOW",
        "MEDIUM",
        "HIGH",
        "HIGHER",
        "MAX",
    )
)


def serialize_json(value: H264AdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> H264AdaptiveQuantization:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264AdaptiveQuantization value: {data!r}")
    return cast(H264AdaptiveQuantization, data)
