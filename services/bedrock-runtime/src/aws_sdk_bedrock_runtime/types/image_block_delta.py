"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ImageBlockDelta``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.error_block
    import aws_sdk_bedrock_runtime.types.image_source


class ImageBlockDelta(TypedDict, closed=True):
    source: NotRequired["aws_sdk_bedrock_runtime.types.image_source.ImageSource"]
    """<p>The incremental image source data for this delta event.</p>"""
    error: NotRequired["aws_sdk_bedrock_runtime.types.error_block.ErrorBlock"]
    """<p>Error information if this image delta could not be processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageBlockDelta) -> dict:
    out: dict = {}
    if "source" in value:
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


def deserialize_json(data: dict) -> ImageBlockDelta:
    out: ImageBlockDelta = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import aws_sdk_bedrock_runtime.types.image_source

        out["source"] = aws_sdk_bedrock_runtime.types.image_source.deserialize_json(
            data["source"]
        )
    if "error" in data:
        import aws_sdk_bedrock_runtime.types.error_block

        out["error"] = aws_sdk_bedrock_runtime.types.error_block.deserialize_json(
            data["error"]
        )
    return out
