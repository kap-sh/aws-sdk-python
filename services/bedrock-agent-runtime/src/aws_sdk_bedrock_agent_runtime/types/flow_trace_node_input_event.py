"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeInputEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_fields
    import aws_sdk_bedrock_agent_runtime.types.node_name


class FlowTraceNodeInputEvent(TypedDict, closed=True):
    node_name: "aws_sdk_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node that received the input.</p>"""
    timestamp: "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The date and time that the trace was returned.</p>"""
    fields: "aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_fields.FlowTraceNodeInputFields"
    """<p>An array of objects containing information about each field in the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeInputEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp

    out["timestamp"] = (
        aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(
            value["timestamp"]
        )
    )
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_fields

    out["fields"] = (
        aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_fields.serialize_json(
            value["fields"]
        )
    )
    return out


def deserialize_json(data: dict) -> FlowTraceNodeInputEvent:
    out: FlowTraceNodeInputEvent = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("FlowTraceNodeInputEvent.node_name required")
    if "timestamp" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["timestamp"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("FlowTraceNodeInputEvent.timestamp required")
    if "fields" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_fields

        out["fields"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_fields.deserialize_json(
                data["fields"]
            )
        )
    else:
        raise DeserializationError("FlowTraceNodeInputEvent.fields required")
    return out
