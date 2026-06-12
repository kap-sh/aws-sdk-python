"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowFailureEvent``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.flow_error_code

class FlowFailureEvent(TypedDict):
    timestamp: "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the failure occurred.</p>"""
    error_code: "aws_sdk_bedrock_agent_runtime.types.flow_error_code.FlowErrorCode"
    """<p>The error code that identifies the type of failure that occurred.</p>"""
    error_message: "str"
    """<p>A descriptive message that provides details about the failure.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: FlowFailureEvent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    out["timestamp"] = aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(value["timestamp"])
    import aws_sdk_bedrock_agent_runtime.types.flow_error_code
    out["errorCode"] = aws_sdk_bedrock_agent_runtime.types.flow_error_code.serialize_json(value["error_code"])
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FlowFailureEvent:
    out: FlowFailureEvent = {}  # type: ignore[typeddict-item]
    if "timestamp" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp
        out["timestamp"] = aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(data["timestamp"])
    else:
        raise DeserializationError("FlowFailureEvent.timestamp required")
    if "errorCode" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_error_code
        out["error_code"] = aws_sdk_bedrock_agent_runtime.types.flow_error_code.deserialize_json(data["errorCode"])
    else:
        raise DeserializationError("FlowFailureEvent.error_code required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError("FlowFailureEvent.error_message required")
    return out