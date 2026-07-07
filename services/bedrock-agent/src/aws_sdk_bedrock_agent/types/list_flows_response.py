"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListFlowsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_summaries
    import aws_sdk_bedrock_agent.types.next_token


class ListFlowsResponse(TypedDict, closed=True):
    flow_summaries: "aws_sdk_bedrock_agent.types.flow_summaries.FlowSummaries"
    """<p>A list, each member of which contains information about a flow.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.flow_summaries

    out["flowSummaries"] = aws_sdk_bedrock_agent.types.flow_summaries.serialize_json(
        value["flow_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFlowsResponse:
    out: ListFlowsResponse = {}  # type: ignore[typeddict-item]
    if "flowSummaries" in data:
        import aws_sdk_bedrock_agent.types.flow_summaries

        out["flow_summaries"] = (
            aws_sdk_bedrock_agent.types.flow_summaries.deserialize_json(
                data["flowSummaries"]
            )
        )
    else:
        raise DeserializationError("ListFlowsResponse.flow_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
