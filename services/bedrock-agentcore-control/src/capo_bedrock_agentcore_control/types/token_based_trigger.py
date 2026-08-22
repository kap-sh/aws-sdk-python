"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TokenBasedTrigger``."""

from typing_extensions import NotRequired, TypedDict


class TokenBasedTrigger(TypedDict, closed=True):
    token_count: NotRequired["int"]
    """<p>Number of tokens that trigger memory processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TokenBasedTrigger) -> dict:
    out: dict = {}
    if "token_count" in value:
        out["tokenCount"] = value["token_count"]
    return out


def deserialize_json(data: dict) -> TokenBasedTrigger:
    out: TokenBasedTrigger = {}  # type: ignore[typeddict-item]
    if data.get("tokenCount") is not None:
        out["token_count"] = data["tokenCount"]
    return out
