"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#SearchResultContentBlock``."""

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError


class SearchResultContentBlock(TypedDict, closed=True):
    text: "str"
    """<p>The actual text content</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResultContentBlock) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> SearchResultContentBlock:
    out: SearchResultContentBlock = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    else:
        raise DeserializationError("SearchResultContentBlock.text required")
    return out
