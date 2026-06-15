"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TokenBasedTriggerInput``."""

from typing import TypedDict


class TokenBasedTriggerInput(TypedDict):
    token_count: "int"
    """<p>Number of tokens that trigger memory processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TokenBasedTriggerInput) -> dict:
    out: dict = {}
    out["tokenCount"] = value.get("token_count", 5000)
    return out


def deserialize_json(data: dict) -> TokenBasedTriggerInput:
    out: TokenBasedTriggerInput = {}  # type: ignore[typeddict-item]
    if "tokenCount" in data:
        out["token_count"] = data["tokenCount"]
    else:
        out["token_count"] = 5000
    return out
