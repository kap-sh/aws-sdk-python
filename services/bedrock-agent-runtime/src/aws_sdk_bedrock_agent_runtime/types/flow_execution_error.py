"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_error_type
    import aws_sdk_bedrock_agent_runtime.types.node_name

class FlowExecutionError(TypedDict):
    node_name: NotRequired["aws_sdk_bedrock_agent_runtime.types.node_name.NodeName"]
    """<p>The name of the node in the flow where the error occurred (if applicable).</p>"""
    error: NotRequired["aws_sdk_bedrock_agent_runtime.types.flow_execution_error_type.FlowExecutionErrorType"]
    """<p>The error code for the type of error that occurred.</p>"""
    message: NotRequired["str"]
    """<p>A descriptive message that provides details about the error.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionError) -> dict:
    out: dict = {}
    if "node_name" in value:
        out["nodeName"] = value["node_name"]
    if "error" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_execution_error_type
        out["error"] = aws_sdk_bedrock_agent_runtime.types.flow_execution_error_type.serialize_json(value["error"])
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> FlowExecutionError:
    out: FlowExecutionError = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    if "error" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_execution_error_type
        out["error"] = aws_sdk_bedrock_agent_runtime.types.flow_execution_error_type.deserialize_json(data["error"])
    if "message" in data:
        out["message"] = data["message"]
    return out