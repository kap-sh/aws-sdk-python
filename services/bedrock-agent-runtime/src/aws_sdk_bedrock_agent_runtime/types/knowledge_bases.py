"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base

KnowledgeBases: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.knowledge_base.KnowledgeBase"
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBases) -> list:
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.knowledge_base.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KnowledgeBases:
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base

    out: KnowledgeBases = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.knowledge_base.deserialize_json(item)
        )
    return out
