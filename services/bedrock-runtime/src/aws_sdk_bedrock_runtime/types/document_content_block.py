"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#DocumentContentBlock``."""

from typing import TypeAlias, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError


class _DocumentContentBlock_text(TypedDict):
    text: "str"


DocumentContentBlock: TypeAlias = _DocumentContentBlock_text


# --- restJson1 ser/de ---
def serialize_json(value: DocumentContentBlock) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("DocumentContentBlock: no variant present")


def deserialize_json(data: dict) -> DocumentContentBlock:
    if "text" in data:
        return {"text": data["text"]}
    else:
        raise DeserializationError("DocumentContentBlock: no recognized variant key")
