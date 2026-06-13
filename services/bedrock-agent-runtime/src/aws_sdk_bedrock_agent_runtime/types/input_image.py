"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InputImage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.byte_content_blob
    import aws_sdk_bedrock_agent_runtime.types.input_image_format


class InputImage(TypedDict):
    format: "aws_sdk_bedrock_agent_runtime.types.input_image_format.InputImageFormat"
    """<p>The format of the input image. Supported formats include png, gif, jpeg, and webp.</p>"""
    inline_content: (
        "aws_sdk_bedrock_agent_runtime.types.byte_content_blob.ByteContentBlob"
    )
    """<p>The base64-encoded image data for inline image content. Maximum size is 5MB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputImage) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.input_image_format

    out["format"] = (
        aws_sdk_bedrock_agent_runtime.types.input_image_format.serialize_json(
            value["format"]
        )
    )
    import aws_sdk_bedrock_agent_runtime.types.byte_content_blob

    out["inlineContent"] = (
        aws_sdk_bedrock_agent_runtime.types.byte_content_blob.serialize_json(
            value["inline_content"]
        )
    )
    return out


def deserialize_json(data: dict) -> InputImage:
    out: InputImage = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import aws_sdk_bedrock_agent_runtime.types.input_image_format

        out["format"] = (
            aws_sdk_bedrock_agent_runtime.types.input_image_format.deserialize_json(
                data["format"]
            )
        )
    else:
        raise DeserializationError("InputImage.format required")
    if "inlineContent" in data:
        import aws_sdk_bedrock_agent_runtime.types.byte_content_blob

        out["inline_content"] = (
            aws_sdk_bedrock_agent_runtime.types.byte_content_blob.deserialize_json(
                data["inlineContent"]
            )
        )
    else:
        raise DeserializationError("InputImage.inline_content required")
    return out
