"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Content``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.sensitive_string


class _Content_text(TypedDict):
    text: "aws_sdk_bedrock_agentcore.types.sensitive_string.SensitiveString"


Content: TypeAlias = _Content_text


# --- restJson1 ser/de ---
def serialize_json(value: Content) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("Content: no variant present")


def deserialize_json(data: dict) -> Content:
    if "text" in data:
        return {"text": data["text"]}
    else:
        raise DeserializationError("Content: no recognized variant key")
