"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseRetrievalConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.knowledge_base_vector_search_configuration


class KnowledgeBaseRetrievalConfiguration(TypedDict, closed=True):
    vector_search_configuration: "capo_bedrock_agent_runtime.types.knowledge_base_vector_search_configuration.KnowledgeBaseVectorSearchConfiguration"
    r"""<p>Contains details about how the results from the vector search should be returned. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html\">Query configurations</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseRetrievalConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.knowledge_base_vector_search_configuration

    out["vectorSearchConfiguration"] = (
        capo_bedrock_agent_runtime.types.knowledge_base_vector_search_configuration.serialize_json(
            value["vector_search_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseRetrievalConfiguration:
    out: KnowledgeBaseRetrievalConfiguration = {}  # type: ignore[typeddict-item]
    if "vectorSearchConfiguration" in data:
        import capo_bedrock_agent_runtime.types.knowledge_base_vector_search_configuration

        out["vector_search_configuration"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_vector_search_configuration.deserialize_json(
                data["vectorSearchConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "KnowledgeBaseRetrievalConfiguration.vector_search_configuration required"
        )
    return out
