"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceEvent``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_trace

class FlowTraceEvent(TypedDict):
    trace: "aws_sdk_bedrock_agent_runtime.types.flow_trace.FlowTrace"
    """<p>The trace object containing information about an input or output for a node in the flow.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceEvent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.flow_trace
    out["trace"] = aws_sdk_bedrock_agent_runtime.types.flow_trace.serialize_json(value["trace"])
    return out


def deserialize_json(data: dict) -> FlowTraceEvent:
    out: FlowTraceEvent = {}  # type: ignore[typeddict-item]
    if "trace" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace
        out["trace"] = aws_sdk_bedrock_agent_runtime.types.flow_trace.deserialize_json(data["trace"])
    else:
        raise DeserializationError("FlowTraceEvent.trace required")
    return out