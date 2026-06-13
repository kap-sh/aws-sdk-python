"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#VideoSegment``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError


class VideoSegment(TypedDict):
    s3_uri: "str"
    """<p>The S3 URI where this specific video segment is stored in the multimodal storage destination.</p>"""
    summary: NotRequired["str"]
    """<p>A text summary describing the content of the video segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoSegment) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    if "summary" in value:
        out["summary"] = value["summary"]
    return out


def deserialize_json(data: dict) -> VideoSegment:
    out: VideoSegment = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    else:
        raise DeserializationError("VideoSegment.s3_uri required")
    if "summary" in data:
        out["summary"] = data["summary"]
    return out
