"""Generated from Smithy shape ``com.amazonaws.bedrockagent#VideoConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.video_configuration

VideoConfigurations: TypeAlias = list[
    "capo_bedrock_agent.types.video_configuration.VideoConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoConfigurations) -> list:
    import capo_bedrock_agent.types.video_configuration

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.video_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> VideoConfigurations:
    import capo_bedrock_agent.types.video_configuration

    out: VideoConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent.types.video_configuration.deserialize_json(item))
    return out
