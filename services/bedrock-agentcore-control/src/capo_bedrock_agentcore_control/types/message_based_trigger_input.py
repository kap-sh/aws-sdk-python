"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MessageBasedTriggerInput``."""

from typing_extensions import TypedDict


class MessageBasedTriggerInput(TypedDict, closed=True):
    message_count: "int"
    """<p>The number of messages that trigger memory processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageBasedTriggerInput) -> dict:
    out: dict = {}
    out["messageCount"] = value.get("message_count", 6)
    return out


def deserialize_json(data: dict) -> MessageBasedTriggerInput:
    out: MessageBasedTriggerInput = {}  # type: ignore[typeddict-item]
    if data.get("messageCount") is not None:
        out["message_count"] = data["messageCount"]
    else:
        out["message_count"] = 6
    return out
