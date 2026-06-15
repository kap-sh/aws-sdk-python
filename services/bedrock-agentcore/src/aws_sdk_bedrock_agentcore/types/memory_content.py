"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryContent``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.sensitive_string


class _MemoryContent_text(TypedDict):
    text: "aws_sdk_bedrock_agentcore.types.sensitive_string.SensitiveString"


MemoryContent: TypeAlias = _MemoryContent_text


# --- restJson1 ser/de ---
def serialize_json(value: MemoryContent) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("MemoryContent: no variant present")


def deserialize_json(data: dict) -> MemoryContent:
    if "text" in data:
        return {"text": data["text"]}
    else:
        raise DeserializationError("MemoryContent: no recognized variant key")
