"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PostProcessingModelInvocationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.metadata
    import capo_bedrock_agent_runtime.types.post_processing_parsed_response
    import capo_bedrock_agent_runtime.types.raw_response
    import capo_bedrock_agent_runtime.types.reasoning_content_block
    import capo_bedrock_agent_runtime.types.trace_id


class PostProcessingModelInvocationOutput(TypedDict, closed=True):
    trace_id: NotRequired["capo_bedrock_agent_runtime.types.trace_id.TraceId"]
    """<p>The unique identifier of the trace.</p>"""
    parsed_response: NotRequired[
        "capo_bedrock_agent_runtime.types.post_processing_parsed_response.PostProcessingParsedResponse"
    ]
    """<p>Details about the response from the Lambda parsing of the output of the post-processing step.</p>"""
    raw_response: NotRequired[
        "capo_bedrock_agent_runtime.types.raw_response.RawResponse"
    ]
    """<p> Details of the raw response from the foundation model output. </p>"""
    metadata: NotRequired["capo_bedrock_agent_runtime.types.metadata.Metadata"]
    """<p> Contains information about the foundation model output from the post-processing step. </p>"""
    reasoning_content: NotRequired[
        "capo_bedrock_agent_runtime.types.reasoning_content_block.ReasoningContentBlock"
    ]
    """<p>Contains content about the reasoning that the model made during the post-processing step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostProcessingModelInvocationOutput) -> dict:
    out: dict = {}
    if "trace_id" in value:
        out["traceId"] = value["trace_id"]
    if "parsed_response" in value:
        import capo_bedrock_agent_runtime.types.post_processing_parsed_response

        out["parsedResponse"] = (
            capo_bedrock_agent_runtime.types.post_processing_parsed_response.serialize_json(
                value["parsed_response"]
            )
        )
    if "raw_response" in value:
        import capo_bedrock_agent_runtime.types.raw_response

        out["rawResponse"] = (
            capo_bedrock_agent_runtime.types.raw_response.serialize_json(
                value["raw_response"]
            )
        )
    if "metadata" in value:
        import capo_bedrock_agent_runtime.types.metadata

        out["metadata"] = capo_bedrock_agent_runtime.types.metadata.serialize_json(
            value["metadata"]
        )
    if "reasoning_content" in value:
        import capo_bedrock_agent_runtime.types.reasoning_content_block

        out["reasoningContent"] = (
            capo_bedrock_agent_runtime.types.reasoning_content_block.serialize_json(
                value["reasoning_content"]
            )
        )
    return out


def deserialize_json(data: dict) -> PostProcessingModelInvocationOutput:
    out: PostProcessingModelInvocationOutput = {}  # type: ignore[typeddict-item]
    if data.get("traceId") is not None:
        out["trace_id"] = data["traceId"]
    if data.get("parsedResponse") is not None:
        import capo_bedrock_agent_runtime.types.post_processing_parsed_response

        out["parsed_response"] = (
            capo_bedrock_agent_runtime.types.post_processing_parsed_response.deserialize_json(
                data["parsedResponse"]
            )
        )
    if data.get("rawResponse") is not None:
        import capo_bedrock_agent_runtime.types.raw_response

        out["raw_response"] = (
            capo_bedrock_agent_runtime.types.raw_response.deserialize_json(
                data["rawResponse"]
            )
        )
    if data.get("metadata") is not None:
        import capo_bedrock_agent_runtime.types.metadata

        out["metadata"] = capo_bedrock_agent_runtime.types.metadata.deserialize_json(
            data["metadata"]
        )
    if data.get("reasoningContent") is not None:
        import capo_bedrock_agent_runtime.types.reasoning_content_block

        out["reasoning_content"] = (
            capo_bedrock_agent_runtime.types.reasoning_content_block.deserialize_json(
                data["reasoningContent"]
            )
        )
    return out
