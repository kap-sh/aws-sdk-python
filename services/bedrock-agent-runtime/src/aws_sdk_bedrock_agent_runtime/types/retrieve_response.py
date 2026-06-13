"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.guadrail_action
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_results
    import aws_sdk_bedrock_agent_runtime.types.next_token


class RetrieveResponse(TypedDict):
    retrieval_results: "aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_results.KnowledgeBaseRetrievalResults"
    """<p>A list of results from querying the knowledge base.</p>"""
    guardrail_action: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guadrail_action.GuadrailAction"
    ]
    """<p>Specifies if there is a guardrail intervention in the response.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>If there are more results than can fit in the response, the response returns a <code>nextToken</code>. Use this token in the <code>nextToken</code> field of another request to retrieve the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_results

    out["retrievalResults"] = (
        aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_results.serialize_json(
            value["retrieval_results"]
        )
    )
    if "guardrail_action" in value:
        import aws_sdk_bedrock_agent_runtime.types.guadrail_action

        out["guardrailAction"] = (
            aws_sdk_bedrock_agent_runtime.types.guadrail_action.serialize_json(
                value["guardrail_action"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> RetrieveResponse:
    out: RetrieveResponse = {}  # type: ignore[typeddict-item]
    if "retrievalResults" in data:
        import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_results

        out["retrieval_results"] = (
            aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_results.deserialize_json(
                data["retrievalResults"]
            )
        )
    else:
        raise DeserializationError("RetrieveResponse.retrieval_results required")
    if "guardrailAction" in data:
        import aws_sdk_bedrock_agent_runtime.types.guadrail_action

        out["guardrail_action"] = (
            aws_sdk_bedrock_agent_runtime.types.guadrail_action.deserialize_json(
                data["guardrailAction"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
