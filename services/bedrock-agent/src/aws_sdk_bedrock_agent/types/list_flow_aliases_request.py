"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListFlowAliasesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_identifier
    import aws_sdk_bedrock_agent.types.max_results
    import aws_sdk_bedrock_agent.types.next_token


class ListFlowAliasesRequest(TypedDict):
    flow_identifier: "aws_sdk_bedrock_agent.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow for which aliases are being returned.</p>"""
    max_results: NotRequired["aws_sdk_bedrock_agent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowAliasesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFlowAliasesRequest:
    out: ListFlowAliasesRequest = {}  # type: ignore[typeddict-item]
    return out
