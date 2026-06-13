"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBase``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_id
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration
    import aws_sdk_bedrock_agent_runtime.types.resource_description


class KnowledgeBase(TypedDict):
    knowledge_base_id: (
        "aws_sdk_bedrock_agent_runtime.types.knowledge_base_id.KnowledgeBaseId"
    )
    """<p> The unique identifier for a knowledge base associated with the inline agent. </p>"""
    description: (
        "aws_sdk_bedrock_agent_runtime.types.resource_description.ResourceDescription"
    )
    """<p> The description of the knowledge base associated with the inline agent. </p>"""
    retrieval_configuration: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.KnowledgeBaseRetrievalConfiguration"
    ]
    """<p> The configurations to apply to the knowledge base during query. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html\">Query configurations</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBase) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["description"] = value["description"]
    if "retrieval_configuration" in value:
        import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration

        out["retrievalConfiguration"] = (
            aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.serialize_json(
                value["retrieval_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBase:
    out: KnowledgeBase = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("KnowledgeBase.knowledge_base_id required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("KnowledgeBase.description required")
    if "retrievalConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration

        out["retrieval_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.deserialize_json(
                data["retrievalConfiguration"]
            )
        )
    return out
