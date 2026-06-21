"""Generated from Smithy shape ``com.amazonaws.medialive#VideoDescriptionScalingBehavior``."""

from typing import Literal, TypeAlias, cast

"""Video Description Scaling Behavior"""
VideoDescriptionScalingBehavior: TypeAlias = Literal[
    "DEFAULT",
    "STRETCH_TO_OUTPUT",
    "SMART_CROP",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoDescriptionScalingBehavior) -> str:
    return value


def deserialize_json(data: str) -> VideoDescriptionScalingBehavior:
    return cast(VideoDescriptionScalingBehavior, data)
