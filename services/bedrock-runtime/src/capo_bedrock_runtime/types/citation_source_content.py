"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CitationSourceContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError


class _CitationSourceContent_text(TypedDict, closed=True):
    text: "str"


CitationSourceContent: TypeAlias = _CitationSourceContent_text


# --- restJson1 ser/de ---
def serialize_json(value: CitationSourceContent) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("CitationSourceContent: no variant present")


def deserialize_json(data: dict) -> CitationSourceContent:
    if data.get("text") is not None:
        return {"text": data["text"]}
    else:
        raise DeserializationError("CitationSourceContent: no recognized variant key")
