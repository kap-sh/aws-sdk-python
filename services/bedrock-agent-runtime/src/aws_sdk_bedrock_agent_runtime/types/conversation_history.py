"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ConversationHistory``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.messages


class ConversationHistory(TypedDict):
    messages: NotRequired["aws_sdk_bedrock_agent_runtime.types.messages.Messages"]
    """<p>The conversation's messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationHistory) -> dict:
    out: dict = {}
    if "messages" in value:
        import aws_sdk_bedrock_agent_runtime.types.messages

        out["messages"] = aws_sdk_bedrock_agent_runtime.types.messages.serialize_json(
            value["messages"]
        )
    return out


def deserialize_json(data: dict) -> ConversationHistory:
    out: ConversationHistory = {}  # type: ignore[typeddict-item]
    if "messages" in data:
        import aws_sdk_bedrock_agent_runtime.types.messages

        out["messages"] = aws_sdk_bedrock_agent_runtime.types.messages.deserialize_json(
            data["messages"]
        )
    return out
