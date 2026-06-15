"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessSlidingWindowConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class HarnessSlidingWindowConfiguration(TypedDict):
    messages_count: NotRequired["int"]
    """<p>The number of recent messages to retain in the context window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSlidingWindowConfiguration) -> dict:
    out: dict = {}
    if "messages_count" in value:
        out["messagesCount"] = value["messages_count"]
    return out


def deserialize_json(data: dict) -> HarnessSlidingWindowConfiguration:
    out: HarnessSlidingWindowConfiguration = {}  # type: ignore[typeddict-item]
    if "messagesCount" in data:
        out["messages_count"] = data["messagesCount"]
    return out
