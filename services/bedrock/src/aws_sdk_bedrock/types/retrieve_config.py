"""Generated from Smithy shape ``com.amazonaws.bedrock#RetrieveConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.knowledge_base_id
    import aws_sdk_bedrock.types.knowledge_base_retrieval_configuration


class RetrieveConfig(TypedDict):
    knowledge_base_id: "aws_sdk_bedrock.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The unique identifier of the knowledge base.</p>"""
    knowledge_base_retrieval_configuration: "aws_sdk_bedrock.types.knowledge_base_retrieval_configuration.KnowledgeBaseRetrievalConfiguration"
    """<p>Contains configuration details for knowledge base retrieval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveConfig) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    import aws_sdk_bedrock.types.knowledge_base_retrieval_configuration

    out["knowledgeBaseRetrievalConfiguration"] = (
        aws_sdk_bedrock.types.knowledge_base_retrieval_configuration.serialize_json(
            value["knowledge_base_retrieval_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> RetrieveConfig:
    out: RetrieveConfig = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("RetrieveConfig.knowledge_base_id required")
    if "knowledgeBaseRetrievalConfiguration" in data:
        import aws_sdk_bedrock.types.knowledge_base_retrieval_configuration

        out["knowledge_base_retrieval_configuration"] = (
            aws_sdk_bedrock.types.knowledge_base_retrieval_configuration.deserialize_json(
                data["knowledgeBaseRetrievalConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RetrieveConfig.knowledge_base_retrieval_configuration required"
        )
    return out
