"""Generated from Smithy shape ``com.amazonaws.bedrock#KnowledgeBaseRetrievalConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.knowledge_base_vector_search_configuration


class KnowledgeBaseRetrievalConfiguration(TypedDict):
    vector_search_configuration: "aws_sdk_bedrock.types.knowledge_base_vector_search_configuration.KnowledgeBaseVectorSearchConfiguration"
    """<p>Contains configuration details for returning the results from the vector search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseRetrievalConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.knowledge_base_vector_search_configuration

    out["vectorSearchConfiguration"] = (
        aws_sdk_bedrock.types.knowledge_base_vector_search_configuration.serialize_json(
            value["vector_search_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseRetrievalConfiguration:
    out: KnowledgeBaseRetrievalConfiguration = {}  # type: ignore[typeddict-item]
    if "vectorSearchConfiguration" in data:
        import aws_sdk_bedrock.types.knowledge_base_vector_search_configuration

        out["vector_search_configuration"] = (
            aws_sdk_bedrock.types.knowledge_base_vector_search_configuration.deserialize_json(
                data["vectorSearchConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "KnowledgeBaseRetrievalConfiguration.vector_search_configuration required"
        )
    return out
