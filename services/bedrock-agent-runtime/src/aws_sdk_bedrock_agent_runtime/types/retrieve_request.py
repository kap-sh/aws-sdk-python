"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_configuration
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_id
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_query
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration
    import aws_sdk_bedrock_agent_runtime.types.next_token


class RetrieveRequest(TypedDict):
    knowledge_base_id: (
        "aws_sdk_bedrock_agent_runtime.types.knowledge_base_id.KnowledgeBaseId"
    )
    """<p>The unique identifier of the knowledge base to query.</p>"""
    retrieval_query: (
        "aws_sdk_bedrock_agent_runtime.types.knowledge_base_query.KnowledgeBaseQuery"
    )
    """<p>Contains the query to send the knowledge base.</p>"""
    retrieval_configuration: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.KnowledgeBaseRetrievalConfiguration"
    ]
    """<p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html\">Query configurations</a>.</p>"""
    guardrail_configuration: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_configuration.GuardrailConfiguration"
    ]
    """<p>Guardrail settings.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>If there are more results than can fit in the response, the response returns a <code>nextToken</code>. Use this token in the <code>nextToken</code> field of another request to retrieve the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_query

    out["retrievalQuery"] = (
        aws_sdk_bedrock_agent_runtime.types.knowledge_base_query.serialize_json(
            value["retrieval_query"]
        )
    )
    if "retrieval_configuration" in value:
        import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration

        out["retrievalConfiguration"] = (
            aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.serialize_json(
                value["retrieval_configuration"]
            )
        )
    if "guardrail_configuration" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_configuration

        out["guardrailConfiguration"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_configuration.serialize_json(
                value["guardrail_configuration"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> RetrieveRequest:
    out: RetrieveRequest = {}  # type: ignore[typeddict-item]
    if "retrievalQuery" in data:
        import aws_sdk_bedrock_agent_runtime.types.knowledge_base_query

        out["retrieval_query"] = (
            aws_sdk_bedrock_agent_runtime.types.knowledge_base_query.deserialize_json(
                data["retrievalQuery"]
            )
        )
    else:
        raise DeserializationError("RetrieveRequest.retrieval_query required")
    if "retrievalConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration

        out["retrieval_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.deserialize_json(
                data["retrievalConfiguration"]
            )
        )
    if "guardrailConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_configuration

        out["guardrail_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_configuration.deserialize_json(
                data["guardrailConfiguration"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
