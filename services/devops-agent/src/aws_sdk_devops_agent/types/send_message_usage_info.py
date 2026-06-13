"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageUsageInfo``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SendMessageUsageInfo(TypedDict):
    input_tokens: NotRequired["int"]
    """<p>Number of input tokens</p>"""
    output_tokens: NotRequired["int"]
    """<p>Number of output tokens</p>"""
    total_tokens: NotRequired["int"]
    """<p>Total tokens used</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageUsageInfo) -> dict:
    out: dict = {}
    if "input_tokens" in value:
        out["inputTokens"] = value["input_tokens"]
    if "output_tokens" in value:
        out["outputTokens"] = value["output_tokens"]
    if "total_tokens" in value:
        out["totalTokens"] = value["total_tokens"]
    return out


def deserialize_json(data: dict) -> SendMessageUsageInfo:
    out: SendMessageUsageInfo = {}  # type: ignore[typeddict-item]
    if "inputTokens" in data:
        out["input_tokens"] = data["inputTokens"]
    if "outputTokens" in data:
        out["output_tokens"] = data["outputTokens"]
    if "totalTokens" in data:
        out["total_tokens"] = data["totalTokens"]
    return out
