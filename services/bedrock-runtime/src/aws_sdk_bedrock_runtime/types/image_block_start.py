"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ImageBlockStart``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.image_format


class ImageBlockStart(TypedDict):
    format: "aws_sdk_bedrock_runtime.types.image_format.ImageFormat"
    """<p>The format of the image data that will be streamed in subsequent delta events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageBlockStart) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.image_format

    out["format"] = aws_sdk_bedrock_runtime.types.image_format.serialize_json(
        value["format"]
    )
    return out


def deserialize_json(data: dict) -> ImageBlockStart:
    out: ImageBlockStart = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import aws_sdk_bedrock_runtime.types.image_format

        out["format"] = aws_sdk_bedrock_runtime.types.image_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("ImageBlockStart.format required")
    return out
