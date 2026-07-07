"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#VideoBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.video_format
    import aws_sdk_bedrock_runtime.types.video_source


class VideoBlock(TypedDict, closed=True):
    format: "aws_sdk_bedrock_runtime.types.video_format.VideoFormat"
    """<p>The block's format.</p>"""
    source: "aws_sdk_bedrock_runtime.types.video_source.VideoSource"
    """<p>The block's source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoBlock) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.video_format

    out["format"] = aws_sdk_bedrock_runtime.types.video_format.serialize_json(
        value["format"]
    )
    import aws_sdk_bedrock_runtime.types.video_source

    out["source"] = aws_sdk_bedrock_runtime.types.video_source.serialize_json(
        value["source"]
    )
    return out


def deserialize_json(data: dict) -> VideoBlock:
    out: VideoBlock = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import aws_sdk_bedrock_runtime.types.video_format

        out["format"] = aws_sdk_bedrock_runtime.types.video_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("VideoBlock.format required")
    if "source" in data:
        import aws_sdk_bedrock_runtime.types.video_source

        out["source"] = aws_sdk_bedrock_runtime.types.video_source.deserialize_json(
            data["source"]
        )
    else:
        raise DeserializationError("VideoBlock.source required")
    return out
