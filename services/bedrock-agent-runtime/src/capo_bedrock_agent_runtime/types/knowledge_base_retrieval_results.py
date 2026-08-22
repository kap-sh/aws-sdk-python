"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseRetrievalResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.knowledge_base_retrieval_result

KnowledgeBaseRetrievalResults: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.knowledge_base_retrieval_result.KnowledgeBaseRetrievalResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseRetrievalResults) -> list:
    import capo_bedrock_agent_runtime.types.knowledge_base_retrieval_result

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.knowledge_base_retrieval_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> KnowledgeBaseRetrievalResults:
    import capo_bedrock_agent_runtime.types.knowledge_base_retrieval_result

    out: KnowledgeBaseRetrievalResults = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.knowledge_base_retrieval_result.deserialize_json(
                item
            )
        )
    return out
