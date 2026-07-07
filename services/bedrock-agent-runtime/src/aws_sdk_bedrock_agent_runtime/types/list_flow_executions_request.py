"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ListFlowExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier
    import aws_sdk_bedrock_agent_runtime.types.flow_identifier
    import aws_sdk_bedrock_agent_runtime.types.max_results
    import aws_sdk_bedrock_agent_runtime.types.next_token


class ListFlowExecutionsRequest(TypedDict, closed=True):
    flow_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier"
    )
    """<p>The unique identifier of the flow to list executions for.</p>"""
    flow_alias_identifier: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier"
    ]
    """<p>The unique identifier of the flow alias to list executions for.</p>"""
    max_results: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.max_results.MaxResults"
    ]
    """<p>The maximum number of flow executions to return in a single response. If more executions exist than the specified <code>maxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>A token to retrieve the next set of results. This value is returned in the response if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowExecutionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFlowExecutionsRequest:
    out: ListFlowExecutionsRequest = {}  # type: ignore[typeddict-item]
    return out
