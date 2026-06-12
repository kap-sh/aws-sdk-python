"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseDocumentDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.knowledge_base_document_detail

KnowledgeBaseDocumentDetails: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.knowledge_base_document_detail.KnowledgeBaseDocumentDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseDocumentDetails) -> list:
    import aws_sdk_bedrock_agent.types.knowledge_base_document_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent.types.knowledge_base_document_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> KnowledgeBaseDocumentDetails:
    import aws_sdk_bedrock_agent.types.knowledge_base_document_detail

    out: KnowledgeBaseDocumentDetails = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.knowledge_base_document_detail.deserialize_json(
                item
            )
        )
    return out
