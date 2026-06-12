"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionInputEvent``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.flow_input_fields
    import aws_sdk_bedrock_agent_runtime.types.node_name

class FlowExecutionInputEvent(TypedDict):
    node_name: "aws_sdk_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node that receives the inputs.</p>"""
    timestamp: "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the inputs are provided.</p>"""
    fields: "aws_sdk_bedrock_agent_runtime.types.flow_input_fields.FlowInputFields"
    """<p>A list of input fields provided to the flow.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionInputEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    out["timestamp"] = aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(value["timestamp"])
    import aws_sdk_bedrock_agent_runtime.types.flow_input_fields
    out["fields"] = aws_sdk_bedrock_agent_runtime.types.flow_input_fields.serialize_json(value["fields"])
    return out


def deserialize_json(data: dict) -> FlowExecutionInputEvent:
    out: FlowExecutionInputEvent = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("FlowExecutionInputEvent.node_name required")
    if "timestamp" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp
        out["timestamp"] = aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(data["timestamp"])
    else:
        raise DeserializationError("FlowExecutionInputEvent.timestamp required")
    if "fields" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_input_fields
        out["fields"] = aws_sdk_bedrock_agent_runtime.types.flow_input_fields.deserialize_json(data["fields"])
    else:
        raise DeserializationError("FlowExecutionInputEvent.fields required")
    return out