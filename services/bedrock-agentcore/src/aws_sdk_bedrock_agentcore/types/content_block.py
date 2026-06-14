"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ContentBlock``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.content_block_type
    import aws_sdk_bedrock_agentcore.types.resource_content


class ContentBlock(TypedDict):
    type: "aws_sdk_bedrock_agentcore.types.content_block_type.ContentBlockType"
    """<p>The type of content in the block.</p>"""
    text: NotRequired["str"]
    """<p>The text content of the block.</p>"""
    data: NotRequired["bytes"]
    """<p>The binary data content of the block.</p>"""
    mime_type: NotRequired["str"]
    """<p>The MIME type of the content.</p>"""
    uri: NotRequired["str"]
    """<p>The URI of the content.</p>"""
    name: NotRequired["str"]
    """<p>The name of the content block.</p>"""
    description: NotRequired["str"]
    """<p>The description of the content block.</p>"""
    size: NotRequired["int"]
    """<p>The size of the content in bytes.</p>"""
    resource: NotRequired[
        "aws_sdk_bedrock_agentcore.types.resource_content.ResourceContent"
    ]
    """<p>The resource associated with the content block.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlock) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.content_block_type

    out["type"] = aws_sdk_bedrock_agentcore.types.content_block_type.serialize_json(
        value["type"]
    )
    if "text" in value:
        out["text"] = value["text"]
    if "data" in value:
        import aws_sdk_bedrock_agentcore.types._prelude.blob

        out["data"] = aws_sdk_bedrock_agentcore.types._prelude.blob.serialize_json(
            value["data"]
        )
    if "mime_type" in value:
        out["mimeType"] = value["mime_type"]
    if "uri" in value:
        out["uri"] = value["uri"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "size" in value:
        out["size"] = value["size"]
    if "resource" in value:
        import aws_sdk_bedrock_agentcore.types.resource_content

        out["resource"] = (
            aws_sdk_bedrock_agentcore.types.resource_content.serialize_json(
                value["resource"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContentBlock:
    out: ContentBlock = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agentcore.types.content_block_type

        out["type"] = (
            aws_sdk_bedrock_agentcore.types.content_block_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("ContentBlock.type required")
    if "text" in data:
        out["text"] = data["text"]
    if "data" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.blob

        out["data"] = aws_sdk_bedrock_agentcore.types._prelude.blob.deserialize_json(
            data["data"]
        )
    if "mimeType" in data:
        out["mime_type"] = data["mimeType"]
    if "uri" in data:
        out["uri"] = data["uri"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "size" in data:
        out["size"] = data["size"]
    if "resource" in data:
        import aws_sdk_bedrock_agentcore.types.resource_content

        out["resource"] = (
            aws_sdk_bedrock_agentcore.types.resource_content.deserialize_json(
                data["resource"]
            )
        )
    return out
