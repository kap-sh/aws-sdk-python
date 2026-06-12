"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HDRToSDRToneMapper``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify how MediaConvert maps brightness and colors from your HDR input to your SDR output. The mode that you select represents a creative choice, with different tradeoffs in the details and tones of your output. To maintain details in bright or saturated areas of your output: Choose Preserve details. For some sources, your SDR output may look less bright and less saturated when compared to your HDR source. MediaConvert automatically applies this mode for HLG sources, regardless of your choice. For a bright and saturated output: Choose Vibrant. We recommend that you choose this mode when any of your source content is HDR10, and for the best results when it is mastered for 1000 nits. You may notice loss of details in bright or saturated areas of your output. HDR to SDR tone mapping has no effect when your input is SDR."""
HDRToSDRToneMapper: TypeAlias = Literal[
    "PRESERVE_DETAILS",
    "VIBRANT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRESERVE_DETAILS",
        "VIBRANT",
    )
)


def serialize_json(value: HDRToSDRToneMapper) -> str:
    return value


def deserialize_json(data: str) -> HDRToSDRToneMapper:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HDRToSDRToneMapper value: {data!r}")
    return cast(HDRToSDRToneMapper, data)
