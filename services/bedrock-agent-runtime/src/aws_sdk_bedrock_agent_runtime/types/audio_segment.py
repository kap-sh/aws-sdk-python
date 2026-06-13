"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AudioSegment``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError


class AudioSegment(TypedDict):
    s3_uri: "str"
    """<p>The S3 URI where this specific audio segment is stored in the multimodal storage destination.</p>"""
    transcription: NotRequired["str"]
    """<p>The text transcription of the audio segment content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioSegment) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    if "transcription" in value:
        out["transcription"] = value["transcription"]
    return out


def deserialize_json(data: dict) -> AudioSegment:
    out: AudioSegment = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    else:
        raise DeserializationError("AudioSegment.s3_uri required")
    if "transcription" in data:
        out["transcription"] = data["transcription"]
    return out
