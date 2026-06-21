"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ScalingBehavior``."""

from typing import Literal, TypeAlias, cast

"""Specify the video Scaling behavior when your output has a different resolution than your input. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/video-scaling.html Select Smart Cropping using Elemental Inference as your scaling behavior to have Elemental Inference automatically crop your video. Smart Crop requires a vertical output aspect ratio (1:1 is the widest aspect ratio supported)."""
ScalingBehavior: TypeAlias = Literal[
    "DEFAULT",
    "STRETCH_TO_OUTPUT",
    "FIT",
    "FIT_NO_UPSCALE",
    "FILL",
    "SMART_CROP",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScalingBehavior) -> str:
    return value


def deserialize_json(data: str) -> ScalingBehavior:
    return cast(ScalingBehavior, data)
