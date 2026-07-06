"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ByteContentDoc``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.byte_content_blob
    import aws_sdk_bedrock_agent_runtime.types.content_type
    import aws_sdk_bedrock_agent_runtime.types.identifier


class ByteContentDoc(TypedDict, closed=True):
    identifier: "aws_sdk_bedrock_agent_runtime.types.identifier.Identifier"
    """<p>The file name of the document contained in the wrapper object.</p>"""
    content_type: "aws_sdk_bedrock_agent_runtime.types.content_type.ContentType"
    """<p>The MIME type of the document contained in the wrapper object.</p>"""
    data: "aws_sdk_bedrock_agent_runtime.types.byte_content_blob.ByteContentBlob"
    """<p>The byte value of the file to upload, encoded as a Base-64 string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ByteContentDoc) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["contentType"] = value["content_type"]
    import aws_sdk_bedrock_agent_runtime.types.byte_content_blob

    out["data"] = aws_sdk_bedrock_agent_runtime.types.byte_content_blob.serialize_json(
        value["data"]
    )
    return out


def deserialize_json(data: dict) -> ByteContentDoc:
    out: ByteContentDoc = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("ByteContentDoc.identifier required")
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    else:
        raise DeserializationError("ByteContentDoc.content_type required")
    if "data" in data:
        import aws_sdk_bedrock_agent_runtime.types.byte_content_blob

        out["data"] = (
            aws_sdk_bedrock_agent_runtime.types.byte_content_blob.deserialize_json(
                data["data"]
            )
        )
    else:
        raise DeserializationError("ByteContentDoc.data required")
    return out
