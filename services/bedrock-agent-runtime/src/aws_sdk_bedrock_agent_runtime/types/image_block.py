"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ImageBlock``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.image_format
    import aws_sdk_bedrock_agent_runtime.types.image_source

class ImageBlock(TypedDict):
    format: "aws_sdk_bedrock_agent_runtime.types.image_format.ImageFormat"
    """<p>The format of the image.</p>"""
    source: "aws_sdk_bedrock_agent_runtime.types.image_source.ImageSource"
    """<p>The source for the image.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ImageBlock) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.image_format
    out["format"] = aws_sdk_bedrock_agent_runtime.types.image_format.serialize_json(value["format"])
    import aws_sdk_bedrock_agent_runtime.types.image_source
    out["source"] = aws_sdk_bedrock_agent_runtime.types.image_source.serialize_json(value["source"])
    return out


def deserialize_json(data: dict) -> ImageBlock:
    out: ImageBlock = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import aws_sdk_bedrock_agent_runtime.types.image_format
        out["format"] = aws_sdk_bedrock_agent_runtime.types.image_format.deserialize_json(data["format"])
    else:
        raise DeserializationError("ImageBlock.format required")
    if "source" in data:
        import aws_sdk_bedrock_agent_runtime.types.image_source
        out["source"] = aws_sdk_bedrock_agent_runtime.types.image_source.deserialize_json(data["source"])
    else:
        raise DeserializationError("ImageBlock.source required")
    return out