"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowMultiTurnInputRequestEvent``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_content
    import aws_sdk_bedrock_agent_runtime.types.node_name
    import aws_sdk_bedrock_agent_runtime.types.node_type

class FlowMultiTurnInputRequestEvent(TypedDict):
    node_name: "aws_sdk_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node in the flow that is requesting the input.</p>"""
    node_type: "aws_sdk_bedrock_agent_runtime.types.node_type.NodeType"
    """<p>The type of the node in the flow that is requesting the input.</p>"""
    content: "aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_content.FlowMultiTurnInputContent"
    """<p>The content payload containing the input request details for the multi-turn interaction.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: FlowMultiTurnInputRequestEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import aws_sdk_bedrock_agent_runtime.types.node_type
    out["nodeType"] = aws_sdk_bedrock_agent_runtime.types.node_type.serialize_json(value["node_type"])
    import aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_content
    out["content"] = aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_content.serialize_json(value["content"])
    return out


def deserialize_json(data: dict) -> FlowMultiTurnInputRequestEvent:
    out: FlowMultiTurnInputRequestEvent = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("FlowMultiTurnInputRequestEvent.node_name required")
    if "nodeType" in data:
        import aws_sdk_bedrock_agent_runtime.types.node_type
        out["node_type"] = aws_sdk_bedrock_agent_runtime.types.node_type.deserialize_json(data["nodeType"])
    else:
        raise DeserializationError("FlowMultiTurnInputRequestEvent.node_type required")
    if "content" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_content
        out["content"] = aws_sdk_bedrock_agent_runtime.types.flow_multi_turn_input_content.deserialize_json(data["content"])
    else:
        raise DeserializationError("FlowMultiTurnInputRequestEvent.content required")
    return out