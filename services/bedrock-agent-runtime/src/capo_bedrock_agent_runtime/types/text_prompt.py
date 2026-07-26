"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TextPrompt``."""

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError


class TextPrompt(TypedDict, closed=True):
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
