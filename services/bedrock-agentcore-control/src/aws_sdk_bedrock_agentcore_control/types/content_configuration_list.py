"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ContentConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.content_configuration

ContentConfigurationList: TypeAlias = list["aws_sdk_bedrock_agentcore_control.types.content_configuration.ContentConfiguration"]


# --- restJson1 ser/de ---
def serialize_json(value: ContentConfigurationList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.content_configuration
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore_control.types.content_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContentConfigurationList:
    import aws_sdk_bedrock_agentcore_control.types.content_configuration
    out: ContentConfigurationList = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore_control.types.content_configuration.deserialize_json(item))
    return out