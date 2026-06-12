"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationBedrockKnowledgeBaseIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.knowledge_base_id

EvaluationBedrockKnowledgeBaseIdentifiers: TypeAlias = list[
    "aws_sdk_bedrock.types.knowledge_base_id.KnowledgeBaseId"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationBedrockKnowledgeBaseIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> EvaluationBedrockKnowledgeBaseIdentifiers:
    return list(data)
