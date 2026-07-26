"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#ListFlowExecutionMessagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.flow_execution_messages
    import capo_iotthingsgraph.types.next_token


class ListFlowExecutionMessagesResponse(TypedDict, closed=True):
    messages: NotRequired[
        "capo_iotthingsgraph.types.flow_execution_messages.FlowExecutionMessages"
    ]
    """<p>A list of objects that contain information about events in the specified flow execution.</p>"""
    next_token: NotRequired["capo_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string to specify as <code>nextToken</code> when you request the next page of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFlowExecutionMessagesResponse) -> dict:
    out: dict = {}
    if "messages" in value:
        import capo_iotthingsgraph.types.flow_execution_messages

        out["messages"] = (
            capo_iotthingsgraph.types.flow_execution_messages.serialize_aws_json_1_1(
                value["messages"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFlowExecutionMessagesResponse:
    out: ListFlowExecutionMessagesResponse = {}  # type: ignore[typeddict-item]
    if "messages" in data:
        import capo_iotthingsgraph.types.flow_execution_messages

        out["messages"] = (
            capo_iotthingsgraph.types.flow_execution_messages.deserialize_aws_json_1_1(
                data["messages"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
