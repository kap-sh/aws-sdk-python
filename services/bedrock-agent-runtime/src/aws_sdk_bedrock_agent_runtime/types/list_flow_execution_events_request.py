"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ListFlowExecutionEventsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_event_type
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_identifier
    import aws_sdk_bedrock_agent_runtime.types.flow_identifier
    import aws_sdk_bedrock_agent_runtime.types.max_results
    import aws_sdk_bedrock_agent_runtime.types.next_token


class ListFlowExecutionEventsRequest(TypedDict):
    flow_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier"
    )
    """<p>The unique identifier of the flow.</p>"""
    flow_alias_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier"
    )
    """<p>The unique identifier of the flow alias used for the execution.</p>"""
    execution_identifier: "aws_sdk_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier"
    """<p>The unique identifier of the flow execution.</p>"""
    max_results: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.max_results.MaxResults"
    ]
    """<p>The maximum number of events to return in a single response. If more events exist than the specified maxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>A token to retrieve the next set of results. This value is returned in the response if more results are available.</p>"""
    event_type: "aws_sdk_bedrock_agent_runtime.types.flow_execution_event_type.FlowExecutionEventType"
    """<p>The type of events to retrieve. Specify <code>Node</code> for node-level events or <code>Flow</code> for flow-level events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowExecutionEventsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFlowExecutionEventsRequest:
    out: ListFlowExecutionEventsRequest = {}  # type: ignore[typeddict-item]
    return out
