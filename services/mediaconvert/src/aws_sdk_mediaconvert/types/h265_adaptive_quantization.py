"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265AdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When you set Adaptive Quantization to Auto, or leave blank, MediaConvert automatically applies quantization to improve the video quality of your output. Set Adaptive Quantization to Low, Medium, High, Higher, or Max to manually control the strength of the quantization filter. When you do, you can specify a value for Spatial Adaptive Quantization, Temporal Adaptive Quantization, and Flicker Adaptive Quantization, to further control the quantization filter. Set Adaptive Quantization to Off to apply no quantization to your output."""
H265AdaptiveQuantization: TypeAlias = Literal[
    "OFF",
    "LOW",
    "MEDIUM",
    "HIGH",
    "HIGHER",
    "MAX",
    "AUTO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "LOW",
        "MEDIUM",
        "HIGH",
        "HIGHER",
        "MAX",
        "AUTO",
    )
)


def serialize_json(value: H265AdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> H265AdaptiveQuantization:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265AdaptiveQuantization value: {data!r}")
    return cast(H265AdaptiveQuantization, data)
