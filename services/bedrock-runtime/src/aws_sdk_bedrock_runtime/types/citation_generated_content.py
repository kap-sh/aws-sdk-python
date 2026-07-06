"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CitationGeneratedContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError


class _CitationGeneratedContent_text(TypedDict, closed=True):
    text: "str"


CitationGeneratedContent: TypeAlias = _CitationGeneratedContent_text


# --- restJson1 ser/de ---
def serialize_json(value: CitationGeneratedContent) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("CitationGeneratedContent: no variant present")


def deserialize_json(data: dict) -> CitationGeneratedContent:
    if "text" in data:
        return {"text": data["text"]}
    else:
        raise DeserializationError(
            "CitationGeneratedContent: no recognized variant key"
        )
