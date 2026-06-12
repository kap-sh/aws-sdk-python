"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ImageInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.image_input_format
    import aws_sdk_bedrock_agent_runtime.types.image_input_source

class ImageInput(TypedDict):
    format: "aws_sdk_bedrock_agent_runtime.types.image_input_format.ImageInputFormat"
    """<p>The type of image in the result.</p>"""
    source: "aws_sdk_bedrock_agent_runtime.types.image_input_source.ImageInputSource"
    """<p>The source of the image in the result.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ImageInput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.image_input_format
    out["format"] = aws_sdk_bedrock_agent_runtime.types.image_input_format.serialize_json(value["format"])
    import aws_sdk_bedrock_agent_runtime.types.image_input_source
    out["source"] = aws_sdk_bedrock_agent_runtime.types.image_input_source.serialize_json(value["source"])
    return out


def deserialize_json(data: dict) -> ImageInput:
    out: ImageInput = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import aws_sdk_bedrock_agent_runtime.types.image_input_format
        out["format"] = aws_sdk_bedrock_agent_runtime.types.image_input_format.deserialize_json(data["format"])
    else:
        raise DeserializationError("ImageInput.format required")
    if "source" in data:
        import aws_sdk_bedrock_agent_runtime.types.image_input_source
        out["source"] = aws_sdk_bedrock_agent_runtime.types.image_input_source.deserialize_json(data["source"])
    else:
        raise DeserializationError("ImageInput.source required")
    return out