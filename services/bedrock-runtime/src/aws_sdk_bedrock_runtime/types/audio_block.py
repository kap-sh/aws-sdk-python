"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AudioBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.audio_format
    import aws_sdk_bedrock_runtime.types.audio_source
    import aws_sdk_bedrock_runtime.types.error_block


class AudioBlock(TypedDict, closed=True):
    format: "aws_sdk_bedrock_runtime.types.audio_format.AudioFormat"
    """<p>The format of the audio data, such as MP3, WAV, FLAC, or other supported audio formats.</p>"""
    source: "aws_sdk_bedrock_runtime.types.audio_source.AudioSource"
    """<p>The source of the audio data, which can be provided as raw bytes or an S3 location.</p>"""
    error: NotRequired["aws_sdk_bedrock_runtime.types.error_block.ErrorBlock"]
    """<p>Error information if the audio block could not be processed or contains invalid data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioBlock) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.audio_format

    out["format"] = aws_sdk_bedrock_runtime.types.audio_format.serialize_json(
        value["format"]
    )
    import aws_sdk_bedrock_runtime.types.audio_source

    out["source"] = aws_sdk_bedrock_runtime.types.audio_source.serialize_json(
        value["source"]
    )
    if "error" in value:
        import aws_sdk_bedrock_runtime.types.error_block

        out["error"] = aws_sdk_bedrock_runtime.types.error_block.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> AudioBlock:
    out: AudioBlock = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import aws_sdk_bedrock_runtime.types.audio_format

        out["format"] = aws_sdk_bedrock_runtime.types.audio_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("AudioBlock.format required")
    if "source" in data:
        import aws_sdk_bedrock_runtime.types.audio_source

        out["source"] = aws_sdk_bedrock_runtime.types.audio_source.deserialize_json(
            data["source"]
        )
    else:
        raise DeserializationError("AudioBlock.source required")
    if "error" in data:
        import aws_sdk_bedrock_runtime.types.error_block

        out["error"] = aws_sdk_bedrock_runtime.types.error_block.deserialize_json(
            data["error"]
        )
    return out
