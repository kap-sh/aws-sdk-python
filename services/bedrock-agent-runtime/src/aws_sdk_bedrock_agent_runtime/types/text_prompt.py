"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TextPrompt``."""

from typing import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError


class TextPrompt(TypedDict):
    text: "str"
    """<p>The text in the text prompt to optimize.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextPrompt) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> TextPrompt:
    out: TextPrompt = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    else:
        raise DeserializationError("TextPrompt.text required")
    return out
