"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ListInvocationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.invocation_summaries
    import aws_sdk_bedrock_agent_runtime.types.next_token


class ListInvocationsResponse(TypedDict):
    invocation_summaries: (
        "aws_sdk_bedrock_agent_runtime.types.invocation_summaries.InvocationSummaries"
    )
    """<p>A list of invocation summaries associated with the session.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvocationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.invocation_summaries

    out["invocationSummaries"] = (
        aws_sdk_bedrock_agent_runtime.types.invocation_summaries.serialize_json(
            value["invocation_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInvocationsResponse:
    out: ListInvocationsResponse = {}  # type: ignore[typeddict-item]
    if "invocationSummaries" in data:
        import aws_sdk_bedrock_agent_runtime.types.invocation_summaries

        out["invocation_summaries"] = (
            aws_sdk_bedrock_agent_runtime.types.invocation_summaries.deserialize_json(
                data["invocationSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListInvocationsResponse.invocation_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
