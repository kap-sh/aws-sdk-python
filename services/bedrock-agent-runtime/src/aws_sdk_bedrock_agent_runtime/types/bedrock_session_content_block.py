"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#BedrockSessionContentBlock``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.image_block

class _BedrockSessionContentBlock_text(TypedDict):
    text: "str"


class _BedrockSessionContentBlock_image(TypedDict):
    image: "aws_sdk_bedrock_agent_runtime.types.image_block.ImageBlock"

BedrockSessionContentBlock: TypeAlias = _BedrockSessionContentBlock_text | _BedrockSessionContentBlock_image

# --- restJson1 ser/de ---
def serialize_json(value: BedrockSessionContentBlock) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "image" in value:
        import aws_sdk_bedrock_agent_runtime.types.image_block
        return {"image": aws_sdk_bedrock_agent_runtime.types.image_block.serialize_json(value["image"])}
    else:
        raise SerializationError("BedrockSessionContentBlock: no variant present")


def deserialize_json(data: dict) -> BedrockSessionContentBlock:
    if "text" in data:
        return {"text": data["text"]}
    elif "image" in data:
        import aws_sdk_bedrock_agent_runtime.types.image_block
        return {"image": aws_sdk_bedrock_agent_runtime.types.image_block.deserialize_json(data["image"])}
    else:
        raise DeserializationError("BedrockSessionContentBlock: no recognized variant key")