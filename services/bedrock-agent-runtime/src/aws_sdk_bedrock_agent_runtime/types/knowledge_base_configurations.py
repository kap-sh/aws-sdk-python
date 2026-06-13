"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_configuration

KnowledgeBaseConfigurations: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.knowledge_base_configuration.KnowledgeBaseConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseConfigurations) -> list:
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.knowledge_base_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> KnowledgeBaseConfigurations:
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_configuration

    out: KnowledgeBaseConfigurations = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.knowledge_base_configuration.deserialize_json(
                item
            )
        )
    return out
