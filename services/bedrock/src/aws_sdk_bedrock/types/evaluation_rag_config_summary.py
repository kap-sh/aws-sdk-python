"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationRagConfigSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_bedrock_knowledge_base_identifiers
    import aws_sdk_bedrock.types.evaluation_precomputed_rag_source_identifiers


class EvaluationRagConfigSummary(TypedDict, closed=True):
    bedrock_knowledge_base_identifiers: NotRequired[
        "aws_sdk_bedrock.types.evaluation_bedrock_knowledge_base_identifiers.EvaluationBedrockKnowledgeBaseIdentifiers"
    ]
    """<p>The Amazon Resource Names (ARNs) of the Knowledge Base resources used for a Knowledge Base evaluation job where Amazon Bedrock invokes the Knowledge Base for you.</p>"""
    precomputed_rag_source_identifiers: NotRequired[
        "aws_sdk_bedrock.types.evaluation_precomputed_rag_source_identifiers.EvaluationPrecomputedRagSourceIdentifiers"
    ]
    """<p>A label that identifies the RAG sources used for a Knowledge Base evaluation job where you provide your own inference response data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationRagConfigSummary) -> dict:
    out: dict = {}
    if "bedrock_knowledge_base_identifiers" in value:
        import aws_sdk_bedrock.types.evaluation_bedrock_knowledge_base_identifiers

        out["bedrockKnowledgeBaseIdentifiers"] = (
            aws_sdk_bedrock.types.evaluation_bedrock_knowledge_base_identifiers.serialize_json(
                value["bedrock_knowledge_base_identifiers"]
            )
        )
    if "precomputed_rag_source_identifiers" in value:
        import aws_sdk_bedrock.types.evaluation_precomputed_rag_source_identifiers

        out["precomputedRagSourceIdentifiers"] = (
            aws_sdk_bedrock.types.evaluation_precomputed_rag_source_identifiers.serialize_json(
                value["precomputed_rag_source_identifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationRagConfigSummary:
    out: EvaluationRagConfigSummary = {}  # type: ignore[typeddict-item]
    if "bedrockKnowledgeBaseIdentifiers" in data:
        import aws_sdk_bedrock.types.evaluation_bedrock_knowledge_base_identifiers

        out["bedrock_knowledge_base_identifiers"] = (
            aws_sdk_bedrock.types.evaluation_bedrock_knowledge_base_identifiers.deserialize_json(
                data["bedrockKnowledgeBaseIdentifiers"]
            )
        )
    if "precomputedRagSourceIdentifiers" in data:
        import aws_sdk_bedrock.types.evaluation_precomputed_rag_source_identifiers

        out["precomputed_rag_source_identifiers"] = (
            aws_sdk_bedrock.types.evaluation_precomputed_rag_source_identifiers.deserialize_json(
                data["precomputedRagSourceIdentifiers"]
            )
        )
    return out
