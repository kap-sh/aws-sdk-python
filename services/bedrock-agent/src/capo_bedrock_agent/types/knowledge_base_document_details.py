"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseDocumentDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.knowledge_base_document_detail

KnowledgeBaseDocumentDetails: TypeAlias = list[
    "capo_bedrock_agent.types.knowledge_base_document_detail.KnowledgeBaseDocumentDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseDocumentDetails) -> list:
    import capo_bedrock_agent.types.knowledge_base_document_detail

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent.types.knowledge_base_document_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KnowledgeBaseDocumentDetails:
    import capo_bedrock_agent.types.knowledge_base_document_detail

    out: KnowledgeBaseDocumentDetails = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent.types.knowledge_base_document_detail.deserialize_json(
                item
            )
        )
    return out
