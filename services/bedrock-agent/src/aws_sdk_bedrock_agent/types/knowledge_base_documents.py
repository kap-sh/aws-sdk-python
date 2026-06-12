"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseDocuments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.knowledge_base_document

KnowledgeBaseDocuments: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.knowledge_base_document.KnowledgeBaseDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseDocuments) -> list:
    import aws_sdk_bedrock_agent.types.knowledge_base_document

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent.types.knowledge_base_document.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KnowledgeBaseDocuments:
    import aws_sdk_bedrock_agent.types.knowledge_base_document

    out: KnowledgeBaseDocuments = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.knowledge_base_document.deserialize_json(item)
        )
    return out
