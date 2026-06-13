"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#PromptVariableValues``."""

from typing import TypeAlias, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError


class _PromptVariableValues_text(TypedDict):
    text: "str"


PromptVariableValues: TypeAlias = _PromptVariableValues_text


# --- restJson1 ser/de ---
def serialize_json(value: PromptVariableValues) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("PromptVariableValues: no variant present")


def deserialize_json(data: dict) -> PromptVariableValues:
    if "text" in data:
        return {"text": data["text"]}
    else:
        raise DeserializationError("PromptVariableValues: no recognized variant key")
