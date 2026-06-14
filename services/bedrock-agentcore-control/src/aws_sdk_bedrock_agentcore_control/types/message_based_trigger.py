"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MessageBasedTrigger``."""

from typing import TypedDict

from typing_extensions import NotRequired


class MessageBasedTrigger(TypedDict):
    message_count: NotRequired["int"]
    """<p>The number of messages that trigger memory processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageBasedTrigger) -> dict:
    out: dict = {}
    if "message_count" in value:
        out["messageCount"] = value["message_count"]
    return out


def deserialize_json(data: dict) -> MessageBasedTrigger:
    out: MessageBasedTrigger = {}  # type: ignore[typeddict-item]
    if "messageCount" in data:
        out["message_count"] = data["messageCount"]
    return out
