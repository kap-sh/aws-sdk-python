"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AudioConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.audio_configuration

AudioConfigurations: TypeAlias = list[
    "capo_bedrock_agent.types.audio_configuration.AudioConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioConfigurations) -> list:
    import capo_bedrock_agent.types.audio_configuration

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.audio_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> AudioConfigurations:
    import capo_bedrock_agent.types.audio_configuration

    out: AudioConfigurations = []
    for item in data:
        out.append(capo_bedrock_agent.types.audio_configuration.deserialize_json(item))
    return out
