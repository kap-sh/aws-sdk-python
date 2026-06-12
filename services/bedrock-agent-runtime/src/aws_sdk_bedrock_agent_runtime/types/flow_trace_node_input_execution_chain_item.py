"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeInputExecutionChainItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_control_node_type
    import aws_sdk_bedrock_agent_runtime.types.node_name

class FlowTraceNodeInputExecutionChainItem(TypedDict):
    node_name: "aws_sdk_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node in the execution chain.</p>"""
    index: NotRequired["int"]
    """<p>The index position of this item in the execution chain.</p>"""
    type: "aws_sdk_bedrock_agent_runtime.types.flow_control_node_type.FlowControlNodeType"
    """<p>The type of execution chain item. Supported values are Iterator and Loop.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeInputExecutionChainItem) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    if "index" in value:
        out["index"] = value["index"]
    import aws_sdk_bedrock_agent_runtime.types.flow_control_node_type
    out["type"] = aws_sdk_bedrock_agent_runtime.types.flow_control_node_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> FlowTraceNodeInputExecutionChainItem:
    out: FlowTraceNodeInputExecutionChainItem = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("FlowTraceNodeInputExecutionChainItem.node_name required")
    if "index" in data:
        out["index"] = data["index"]
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_control_node_type
        out["type"] = aws_sdk_bedrock_agent_runtime.types.flow_control_node_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("FlowTraceNodeInputExecutionChainItem.type required")
    return out