"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RoutingClassifierModelInvocationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.metadata
    import aws_sdk_bedrock_agent_runtime.types.raw_response
    import aws_sdk_bedrock_agent_runtime.types.trace_id


class RoutingClassifierModelInvocationOutput(TypedDict, closed=True):
    trace_id: NotRequired["aws_sdk_bedrock_agent_runtime.types.trace_id.TraceId"]
    """<p>The invocation's trace ID.</p>"""
    raw_response: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.raw_response.RawResponse"
    ]
    """<p>The invocation's raw response.</p>"""
    metadata: NotRequired["aws_sdk_bedrock_agent_runtime.types.metadata.Metadata"]
    """<p>The invocation's metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingClassifierModelInvocationOutput) -> dict:
    out: dict = {}
    if "trace_id" in value:
        out["traceId"] = value["trace_id"]
    if "raw_response" in value:
        import aws_sdk_bedrock_agent_runtime.types.raw_response

        out["rawResponse"] = (
            aws_sdk_bedrock_agent_runtime.types.raw_response.serialize_json(
                value["raw_response"]
            )
        )
    if "metadata" in value:
        import aws_sdk_bedrock_agent_runtime.types.metadata

        out["metadata"] = aws_sdk_bedrock_agent_runtime.types.metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> RoutingClassifierModelInvocationOutput:
    out: RoutingClassifierModelInvocationOutput = {}  # type: ignore[typeddict-item]
    if "traceId" in data:
        out["trace_id"] = data["traceId"]
    if "rawResponse" in data:
        import aws_sdk_bedrock_agent_runtime.types.raw_response

        out["raw_response"] = (
            aws_sdk_bedrock_agent_runtime.types.raw_response.deserialize_json(
                data["rawResponse"]
            )
        )
    if "metadata" in data:
        import aws_sdk_bedrock_agent_runtime.types.metadata

        out["metadata"] = aws_sdk_bedrock_agent_runtime.types.metadata.deserialize_json(
            data["metadata"]
        )
    return out
