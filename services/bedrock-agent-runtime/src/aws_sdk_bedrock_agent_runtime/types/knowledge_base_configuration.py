"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_id
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration


class KnowledgeBaseConfiguration(TypedDict):
    knowledge_base_id: (
        "aws_sdk_bedrock_agent_runtime.types.knowledge_base_id.KnowledgeBaseId"
    )
    """<p>The unique identifier for a knowledge base attached to the agent.</p>"""
    retrieval_configuration: "aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.KnowledgeBaseRetrievalConfiguration"
    r"""<p>The configurations to apply to the knowledge base during query. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html\">Query configurations</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseConfiguration) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration

    out["retrievalConfiguration"] = (
        aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.serialize_json(
            value["retrieval_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseConfiguration:
    out: KnowledgeBaseConfiguration = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError(
            "KnowledgeBaseConfiguration.knowledge_base_id required"
        )
    if "retrievalConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration

        out["retrieval_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.deserialize_json(
                data["retrievalConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "KnowledgeBaseConfiguration.retrieval_configuration required"
        )
    return out
