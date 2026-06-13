"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ListFlowExecutionEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_events
    import aws_sdk_bedrock_agent_runtime.types.next_token


class ListFlowExecutionEventsResponse(TypedDict):
    flow_execution_events: (
        "aws_sdk_bedrock_agent_runtime.types.flow_execution_events.FlowExecutionEvents"
    )
    """<p>A list of events that occurred during the flow execution. Events can include node inputs and outputs, flow inputs and outputs, condition results, and failure events.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>A token to retrieve the next set of results. This value is returned if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowExecutionEventsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_events

    out["flowExecutionEvents"] = (
        aws_sdk_bedrock_agent_runtime.types.flow_execution_events.serialize_json(
            value["flow_execution_events"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFlowExecutionEventsResponse:
    out: ListFlowExecutionEventsResponse = {}  # type: ignore[typeddict-item]
    if "flowExecutionEvents" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_execution_events

        out["flow_execution_events"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_execution_events.deserialize_json(
                data["flowExecutionEvents"]
            )
        )
    else:
        raise DeserializationError(
            "ListFlowExecutionEventsResponse.flow_execution_events required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
