"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ConversationHistory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.messages


class ConversationHistory(TypedDict, closed=True):
    messages: NotRequired["capo_bedrock_agent_runtime.types.messages.Messages"]
    """<p>The conversation's messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationHistory) -> dict:
    out: dict = {}
    if "messages" in value:
        import capo_bedrock_agent_runtime.types.messages

        out["messages"] = capo_bedrock_agent_runtime.types.messages.serialize_json(
            value["messages"]
        )
    return out


def deserialize_json(data: dict) -> ConversationHistory:
    out: ConversationHistory = {}  # type: ignore[typeddict-item]
    if "messages" in data:
        import capo_bedrock_agent_runtime.types.messages

        out["messages"] = capo_bedrock_agent_runtime.types.messages.deserialize_json(
            data["messages"]
        )
    return out
