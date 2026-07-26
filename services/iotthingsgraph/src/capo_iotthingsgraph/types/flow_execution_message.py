"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#FlowExecutionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.flow_execution_event_type
    import capo_iotthingsgraph.types.flow_execution_message_id
    import capo_iotthingsgraph.types.flow_execution_message_payload
    import capo_iotthingsgraph.types.timestamp


class FlowExecutionMessage(TypedDict, closed=True):
    message_id: NotRequired[
        "capo_iotthingsgraph.types.flow_execution_message_id.FlowExecutionMessageId"
    ]
    """<p>The unique identifier of the message.</p>"""
    event_type: NotRequired[
        "capo_iotthingsgraph.types.flow_execution_event_type.FlowExecutionEventType"
    ]
    """<p>The type of flow event .</p>"""
    timestamp: NotRequired["capo_iotthingsgraph.types.timestamp.Timestamp"]
    """<p>The date and time when the message was last updated.</p>"""
    payload: NotRequired[
        "capo_iotthingsgraph.types.flow_execution_message_payload.FlowExecutionMessagePayload"
    ]
    """<p>A string containing information about the flow event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowExecutionMessage) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["messageId"] = value["message_id"]
    if "event_type" in value:
        import capo_iotthingsgraph.types.flow_execution_event_type

        out["eventType"] = (
            capo_iotthingsgraph.types.flow_execution_event_type.serialize_aws_json_1_1(
                value["event_type"]
            )
        )
    if "timestamp" in value:
        import capo_iotthingsgraph.types.timestamp

        out["timestamp"] = capo_iotthingsgraph.types.timestamp.serialize_aws_json_1_1(
            value["timestamp"]
        )
    if "payload" in value:
        out["payload"] = value["payload"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FlowExecutionMessage:
    out: FlowExecutionMessage = {}  # type: ignore[typeddict-item]
    if "messageId" in data:
        out["message_id"] = data["messageId"]
    if "eventType" in data:
        import capo_iotthingsgraph.types.flow_execution_event_type

        out["event_type"] = (
            capo_iotthingsgraph.types.flow_execution_event_type.deserialize_aws_json_1_1(
                data["eventType"]
            )
        )
    if "timestamp" in data:
        import capo_iotthingsgraph.types.timestamp

        out["timestamp"] = capo_iotthingsgraph.types.timestamp.deserialize_aws_json_1_1(
            data["timestamp"]
        )
    if "payload" in data:
        out["payload"] = data["payload"]
    return out
