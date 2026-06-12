"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ByteContentFile``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.byte_content_blob
    import aws_sdk_bedrock_agent_runtime.types.mime_type

class ByteContentFile(TypedDict):
    media_type: "aws_sdk_bedrock_agent_runtime.types.mime_type.MimeType"
    """<p>The MIME type of data contained in the file used for chat.</p>"""
    data: "aws_sdk_bedrock_agent_runtime.types.byte_content_blob.ByteContentBlob"
    """<p>The raw bytes of the file to attach. The maximum size of all files that is attached is 10MB. You can attach a maximum of 5 files. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ByteContentFile) -> dict:
    out: dict = {}
    out["mediaType"] = value["media_type"]
    import aws_sdk_bedrock_agent_runtime.types.byte_content_blob
    out["data"] = aws_sdk_bedrock_agent_runtime.types.byte_content_blob.serialize_json(value["data"])
    return out


def deserialize_json(data: dict) -> ByteContentFile:
    out: ByteContentFile = {}  # type: ignore[typeddict-item]
    if "mediaType" in data:
        out["media_type"] = data["mediaType"]
    else:
        raise DeserializationError("ByteContentFile.media_type required")
    if "data" in data:
        import aws_sdk_bedrock_agent_runtime.types.byte_content_blob
        out["data"] = aws_sdk_bedrock_agent_runtime.types.byte_content_blob.deserialize_json(data["data"])
    else:
        raise DeserializationError("ByteContentFile.data required")
    return out