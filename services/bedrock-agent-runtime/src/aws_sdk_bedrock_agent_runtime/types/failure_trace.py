"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FailureTrace``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.failure_reason_string
    import aws_sdk_bedrock_agent_runtime.types.metadata
    import aws_sdk_bedrock_agent_runtime.types.trace_id


class FailureTrace(TypedDict):
    trace_id: NotRequired["aws_sdk_bedrock_agent_runtime.types.trace_id.TraceId"]
    """<p>The unique identifier of the trace.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.failure_reason_string.FailureReasonString"
    ]
    """<p>The reason the interaction failed.</p>"""
    failure_code: NotRequired["int"]
    """<p>The failure code for the trace.</p>"""
    metadata: NotRequired["aws_sdk_bedrock_agent_runtime.types.metadata.Metadata"]
    """<p>Information about the failure that occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailureTrace) -> dict:
    out: dict = {}
    if "trace_id" in value:
        out["traceId"] = value["trace_id"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    if "metadata" in value:
        import aws_sdk_bedrock_agent_runtime.types.metadata

        out["metadata"] = aws_sdk_bedrock_agent_runtime.types.metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> FailureTrace:
    out: FailureTrace = {}  # type: ignore[typeddict-item]
    if "traceId" in data:
        out["trace_id"] = data["traceId"]
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    if "metadata" in data:
        import aws_sdk_bedrock_agent_runtime.types.metadata

        out["metadata"] = aws_sdk_bedrock_agent_runtime.types.metadata.deserialize_json(
            data["metadata"]
        )
    return out
