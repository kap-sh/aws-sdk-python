"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CustomOrchestrationTrace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.custom_orchestration_trace_event
    import aws_sdk_bedrock_agent_runtime.types.trace_id


class CustomOrchestrationTrace(TypedDict, closed=True):
    trace_id: NotRequired["aws_sdk_bedrock_agent_runtime.types.trace_id.TraceId"]
    """<p> The unique identifier of the trace. </p>"""
    event: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.custom_orchestration_trace_event.CustomOrchestrationTraceEvent"
    ]
    """<p> The event details used with the custom orchestration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomOrchestrationTrace) -> dict:
    out: dict = {}
    if "trace_id" in value:
        out["traceId"] = value["trace_id"]
    if "event" in value:
        import aws_sdk_bedrock_agent_runtime.types.custom_orchestration_trace_event

        out["event"] = (
            aws_sdk_bedrock_agent_runtime.types.custom_orchestration_trace_event.serialize_json(
                value["event"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomOrchestrationTrace:
    out: CustomOrchestrationTrace = {}  # type: ignore[typeddict-item]
    if "traceId" in data:
        out["trace_id"] = data["traceId"]
    if "event" in data:
        import aws_sdk_bedrock_agent_runtime.types.custom_orchestration_trace_event

        out["event"] = (
            aws_sdk_bedrock_agent_runtime.types.custom_orchestration_trace_event.deserialize_json(
                data["event"]
            )
        )
    return out
