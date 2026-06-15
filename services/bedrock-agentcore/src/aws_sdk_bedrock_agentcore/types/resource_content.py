"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ResourceContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.resource_content_type


class ResourceContent(TypedDict):
    type: "aws_sdk_bedrock_agentcore.types.resource_content_type.ResourceContentType"
    """<p>The type of resource content.</p>"""
    uri: NotRequired["str"]
    """<p>The URI of the resource content.</p>"""
    mime_type: NotRequired["str"]
    """<p>The MIME type of the resource content.</p>"""
    text: NotRequired["str"]
    """<p>The text resource content.</p>"""
    blob: NotRequired["bytes"]
    """<p>The binary resource content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceContent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.resource_content_type

    out["type"] = aws_sdk_bedrock_agentcore.types.resource_content_type.serialize_json(
        value["type"]
    )
    if "uri" in value:
        out["uri"] = value["uri"]
    if "mime_type" in value:
        out["mimeType"] = value["mime_type"]
    if "text" in value:
        out["text"] = value["text"]
    if "blob" in value:
        import aws_sdk_bedrock_agentcore.types._prelude.blob

        out["blob"] = aws_sdk_bedrock_agentcore.types._prelude.blob.serialize_json(
            value["blob"]
        )
    return out


def deserialize_json(data: dict) -> ResourceContent:
    out: ResourceContent = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agentcore.types.resource_content_type

        out["type"] = (
            aws_sdk_bedrock_agentcore.types.resource_content_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("ResourceContent.type required")
    if "uri" in data:
        out["uri"] = data["uri"]
    if "mimeType" in data:
        out["mime_type"] = data["mimeType"]
    if "text" in data:
        out["text"] = data["text"]
    if "blob" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.blob

        out["blob"] = aws_sdk_bedrock_agentcore.types._prelude.blob.deserialize_json(
            data["blob"]
        )
    return out
