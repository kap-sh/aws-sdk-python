"""Generated from Smithy shape ``com.amazonaws.bedrockagent#VideoConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.video_configuration

VideoConfigurations: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.video_configuration.VideoConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoConfigurations) -> list:
    import aws_sdk_bedrock_agent.types.video_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.video_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> VideoConfigurations:
    import aws_sdk_bedrock_agent.types.video_configuration

    out: VideoConfigurations = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.video_configuration.deserialize_json(item)
        )
    return out
