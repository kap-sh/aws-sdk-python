"""Generated from Smithy shape ``com.amazonaws.ivs#VideoConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.video_configuration

VideoConfigurationList: TypeAlias = list[
    "aws_sdk_ivs.types.video_configuration.VideoConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoConfigurationList) -> list:
    import aws_sdk_ivs.types.video_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_ivs.types.video_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> VideoConfigurationList:
    import aws_sdk_ivs.types.video_configuration

    out: VideoConfigurationList = []
    for item in data:
        out.append(aws_sdk_ivs.types.video_configuration.deserialize_json(item))
    return out
