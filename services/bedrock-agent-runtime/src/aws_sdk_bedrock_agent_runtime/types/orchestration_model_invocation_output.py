"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OrchestrationModelInvocationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.metadata
    import aws_sdk_bedrock_agent_runtime.types.raw_response
    import aws_sdk_bedrock_agent_runtime.types.reasoning_content_block
    import aws_sdk_bedrock_agent_runtime.types.trace_id


class OrchestrationModelInvocationOutput(TypedDict, closed=True):
    trace_id: NotRequired["aws_sdk_bedrock_agent_runtime.types.trace_id.TraceId"]
    """<p>The unique identifier of the trace.</p>"""
    raw_response: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.raw_response.RawResponse"
    ]
    """<p>Contains details of the raw response from the foundation model output.</p>"""
    metadata: NotRequired["aws_sdk_bedrock_agent_runtime.types.metadata.Metadata"]
    """<p>Contains information about the foundation model output from the orchestration step.</p>"""
    reasoning_content: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.reasoning_content_block.ReasoningContentBlock"
    ]
    """<p>Contains content about the reasoning that the model made during the orchestration step. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrchestrationModelInvocationOutput) -> dict:
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
    if "reasoning_content" in value:
        import aws_sdk_bedrock_agent_runtime.types.reasoning_content_block

        out["reasoningContent"] = (
            aws_sdk_bedrock_agent_runtime.types.reasoning_content_block.serialize_json(
                value["reasoning_content"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrchestrationModelInvocationOutput:
    out: OrchestrationModelInvocationOutput = {}  # type: ignore[typeddict-item]
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
    if "reasoningContent" in data:
        import aws_sdk_bedrock_agent_runtime.types.reasoning_content_block

        out["reasoning_content"] = (
            aws_sdk_bedrock_agent_runtime.types.reasoning_content_block.deserialize_json(
                data["reasoningContent"]
            )
        )
    return out
