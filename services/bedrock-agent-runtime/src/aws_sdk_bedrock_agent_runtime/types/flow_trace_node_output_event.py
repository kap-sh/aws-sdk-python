"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeOutputEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_fields
    import aws_sdk_bedrock_agent_runtime.types.node_name


class FlowTraceNodeOutputEvent(TypedDict):
    node_name: "aws_sdk_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node that yielded the output.</p>"""
    timestamp: "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The date and time that the trace was returned.</p>"""
    fields: "aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_fields.FlowTraceNodeOutputFields"
    """<p>An array of objects containing information about each field in the output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeOutputEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp

    out["timestamp"] = (
        aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(
            value["timestamp"]
        )
    )
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_fields

    out["fields"] = (
        aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_fields.serialize_json(
            value["fields"]
        )
    )
    return out


def deserialize_json(data: dict) -> FlowTraceNodeOutputEvent:
    out: FlowTraceNodeOutputEvent = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("FlowTraceNodeOutputEvent.node_name required")
    if "timestamp" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["timestamp"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("FlowTraceNodeOutputEvent.timestamp required")
    if "fields" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_fields

        out["fields"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_fields.deserialize_json(
                data["fields"]
            )
        )
    else:
        raise DeserializationError("FlowTraceNodeOutputEvent.fields required")
    return out
