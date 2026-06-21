"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vp9FramerateConversionAlgorithm``."""

from typing import Literal, TypeAlias, cast

"""Choose the method that you want MediaConvert to use when increasing or decreasing your video's frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates."""
Vp9FramerateConversionAlgorithm: TypeAlias = Literal[
    "DUPLICATE_DROP",
    "INTERPOLATE",
    "FRAMEFORMER",
    "MAINTAIN_FRAME_COUNT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Vp9FramerateConversionAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> Vp9FramerateConversionAlgorithm:
    return cast(Vp9FramerateConversionAlgorithm, data)
