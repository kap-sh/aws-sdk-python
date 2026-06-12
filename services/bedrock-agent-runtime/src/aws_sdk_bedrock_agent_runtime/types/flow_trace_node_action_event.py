"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeActionEvent``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.node_name

class FlowTraceNodeActionEvent(TypedDict):
    node_name: "aws_sdk_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node that called the operation.</p>"""
    timestamp: "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The date and time that the operation was called.</p>"""
    request_id: "str"
    """<p>The ID of the request that the node made to the operation.</p>"""
    service_name: "str"
    """<p>The name of the service that the node called.</p>"""
    operation_name: "str"
    """<p>The name of the operation that the node called.</p>"""
    operation_request: NotRequired["object"]
    """<p>The request payload sent to the downstream service.</p>"""
    operation_response: NotRequired["object"]
    """<p>The response payload received from the downstream service.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeActionEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    out["timestamp"] = aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(value["timestamp"])
    out["requestId"] = value["request_id"]
    out["serviceName"] = value["service_name"]
    out["operationName"] = value["operation_name"]
    if "operation_request" in value:
        out["operationRequest"] = value["operation_request"]
    if "operation_response" in value:
        out["operationResponse"] = value["operation_response"]
    return out


def deserialize_json(data: dict) -> FlowTraceNodeActionEvent:
    out: FlowTraceNodeActionEvent = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("FlowTraceNodeActionEvent.node_name required")
    if "timestamp" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp
        out["timestamp"] = aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(data["timestamp"])
    else:
        raise DeserializationError("FlowTraceNodeActionEvent.timestamp required")
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("FlowTraceNodeActionEvent.request_id required")
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError("FlowTraceNodeActionEvent.service_name required")
    if "operationName" in data:
        out["operation_name"] = data["operationName"]
    else:
        raise DeserializationError("FlowTraceNodeActionEvent.operation_name required")
    if "operationRequest" in data:
        out["operation_request"] = data["operationRequest"]
    if "operationResponse" in data:
        out["operation_response"] = data["operationResponse"]
    return out