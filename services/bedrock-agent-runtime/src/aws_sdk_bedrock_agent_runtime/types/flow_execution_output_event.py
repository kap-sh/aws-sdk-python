"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionOutputEvent``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.flow_output_fields
    import aws_sdk_bedrock_agent_runtime.types.node_name

class FlowExecutionOutputEvent(TypedDict):
    node_name: "aws_sdk_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node that produces the outputs.</p>"""
    timestamp: "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the outputs are produced.</p>"""
    fields: "aws_sdk_bedrock_agent_runtime.types.flow_output_fields.FlowOutputFields"
    """<p>A list of output fields produced by the flow.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionOutputEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    out["timestamp"] = aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(value["timestamp"])
    import aws_sdk_bedrock_agent_runtime.types.flow_output_fields
    out["fields"] = aws_sdk_bedrock_agent_runtime.types.flow_output_fields.serialize_json(value["fields"])
    return out


def deserialize_json(data: dict) -> FlowExecutionOutputEvent:
    out: FlowExecutionOutputEvent = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("FlowExecutionOutputEvent.node_name required")
    if "timestamp" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp
        out["timestamp"] = aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(data["timestamp"])
    else:
        raise DeserializationError("FlowExecutionOutputEvent.timestamp required")
    if "fields" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_output_fields
        out["fields"] = aws_sdk_bedrock_agent_runtime.types.flow_output_fields.deserialize_json(data["fields"])
    else:
        raise DeserializationError("FlowExecutionOutputEvent.fields required")
    return out