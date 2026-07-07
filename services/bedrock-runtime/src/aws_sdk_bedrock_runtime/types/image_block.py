"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ImageBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.error_block
    import aws_sdk_bedrock_runtime.types.image_format
    import aws_sdk_bedrock_runtime.types.image_source


class ImageBlock(TypedDict, closed=True):
    format: "aws_sdk_bedrock_runtime.types.image_format.ImageFormat"
    """<p>The format of the image.</p>"""
    source: "aws_sdk_bedrock_runtime.types.image_source.ImageSource"
    """<p>The source for the image.</p>"""
    error: NotRequired["aws_sdk_bedrock_runtime.types.error_block.ErrorBlock"]
    """<p>Error information if the image block could not be processed or contains invalid data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageBlock) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.image_format

    out["format"] = aws_sdk_bedrock_runtime.types.image_format.serialize_json(
        value["format"]
    )
    import aws_sdk_bedrock_runtime.types.image_source

    out["source"] = aws_sdk_bedrock_runtime.types.image_source.serialize_json(
        value["source"]
    )
    if "error" in value:
        import aws_sdk_bedrock_runtime.types.error_block

        out["error"] = aws_sdk_bedrock_runtime.types.error_block.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> ImageBlock:
    out: ImageBlock = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import aws_sdk_bedrock_runtime.types.image_format

        out["format"] = aws_sdk_bedrock_runtime.types.image_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("ImageBlock.format required")
    if "source" in data:
        import aws_sdk_bedrock_runtime.types.image_source

        out["source"] = aws_sdk_bedrock_runtime.types.image_source.deserialize_json(
            data["source"]
        )
    else:
        raise DeserializationError("ImageBlock.source required")
    if "error" in data:
        import aws_sdk_bedrock_runtime.types.error_block

        out["error"] = aws_sdk_bedrock_runtime.types.error_block.deserialize_json(
            data["error"]
        )
    return out
