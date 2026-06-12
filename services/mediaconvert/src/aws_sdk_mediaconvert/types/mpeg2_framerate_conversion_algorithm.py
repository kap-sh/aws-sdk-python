"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2FramerateConversionAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates."""
Mpeg2FramerateConversionAlgorithm: TypeAlias = Literal[
    "DUPLICATE_DROP",
    "INTERPOLATE",
    "FRAMEFORMER",
    "MAINTAIN_FRAME_COUNT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DUPLICATE_DROP",
        "INTERPOLATE",
        "FRAMEFORMER",
        "MAINTAIN_FRAME_COUNT",
    )
)


def serialize_json(value: Mpeg2FramerateConversionAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2FramerateConversionAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Mpeg2FramerateConversionAlgorithm value: {data!r}"
        )
    return cast(Mpeg2FramerateConversionAlgorithm, data)
