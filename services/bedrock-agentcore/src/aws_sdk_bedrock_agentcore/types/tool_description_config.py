"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolDescriptionConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.tool_description_text


class _ToolDescriptionConfig_text(TypedDict, closed=True):
    text: "aws_sdk_bedrock_agentcore.types.tool_description_text.ToolDescriptionText"


ToolDescriptionConfig: TypeAlias = _ToolDescriptionConfig_text


# --- restJson1 ser/de ---
def serialize_json(value: ToolDescriptionConfig) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("ToolDescriptionConfig: no variant present")


def deserialize_json(data: dict) -> ToolDescriptionConfig:
    if "text" in data:
        return {"text": data["text"]}
    else:
        raise DeserializationError("ToolDescriptionConfig: no recognized variant key")
