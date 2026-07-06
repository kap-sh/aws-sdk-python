"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Usage``."""

from typing_extensions import NotRequired, TypedDict


class Usage(TypedDict, closed=True):
    input_tokens: NotRequired["int"]
    """<p>Contains information about the input tokens from the foundation model usage.</p>"""
    output_tokens: NotRequired["int"]
    """<p>Contains information about the output tokens from the foundation model usage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Usage) -> dict:
    out: dict = {}
    if "input_tokens" in value:
        out["inputTokens"] = value["input_tokens"]
    if "output_tokens" in value:
        out["outputTokens"] = value["output_tokens"]
    return out


def deserialize_json(data: dict) -> Usage:
    out: Usage = {}  # type: ignore[typeddict-item]
    if "inputTokens" in data:
        out["input_tokens"] = data["inputTokens"]
    if "outputTokens" in data:
        out["output_tokens"] = data["outputTokens"]
    return out
