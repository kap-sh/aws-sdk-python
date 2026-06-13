"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowCompletionEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_completion_reason


class FlowCompletionEvent(TypedDict):
    completion_reason: "aws_sdk_bedrock_agent_runtime.types.flow_completion_reason.FlowCompletionReason"
    """<p>The reason that the flow completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowCompletionEvent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.flow_completion_reason

    out["completionReason"] = (
        aws_sdk_bedrock_agent_runtime.types.flow_completion_reason.serialize_json(
            value["completion_reason"]
        )
    )
    return out


def deserialize_json(data: dict) -> FlowCompletionEvent:
    out: FlowCompletionEvent = {}  # type: ignore[typeddict-item]
    if "completionReason" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_completion_reason

        out["completion_reason"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_completion_reason.deserialize_json(
                data["completionReason"]
            )
        )
    else:
        raise DeserializationError("FlowCompletionEvent.completion_reason required")
    return out
