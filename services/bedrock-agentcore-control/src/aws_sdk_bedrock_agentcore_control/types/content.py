"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Content``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.natural_language

class _Content_rawText(TypedDict):
    rawText: "aws_sdk_bedrock_agentcore_control.types.natural_language.NaturalLanguage"

Content: TypeAlias = _Content_rawText

# --- restJson1 ser/de ---
def serialize_json(value: Content) -> dict:
    if "rawText" in value:
        return {"rawText": value["rawText"]}
    else:
        raise SerializationError("Content: no variant present")


def deserialize_json(data: dict) -> Content:
    if "rawText" in data:
        return {"rawText": data["rawText"]}
    else:
        raise DeserializationError("Content: no recognized variant key")