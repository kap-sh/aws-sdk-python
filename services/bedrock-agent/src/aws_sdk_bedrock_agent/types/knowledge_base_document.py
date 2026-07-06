"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.document_content
    import aws_sdk_bedrock_agent.types.document_metadata


class KnowledgeBaseDocument(TypedDict, closed=True):
    metadata: NotRequired[
        "aws_sdk_bedrock_agent.types.document_metadata.DocumentMetadata"
    ]
    """<p>Contains the metadata to associate with the document.</p>"""
    content: "aws_sdk_bedrock_agent.types.document_content.DocumentContent"
    """<p>Contains the content of the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseDocument) -> dict:
    out: dict = {}
    if "metadata" in value:
        import aws_sdk_bedrock_agent.types.document_metadata

        out["metadata"] = aws_sdk_bedrock_agent.types.document_metadata.serialize_json(
            value["metadata"]
        )
    import aws_sdk_bedrock_agent.types.document_content

    out["content"] = aws_sdk_bedrock_agent.types.document_content.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseDocument:
    out: KnowledgeBaseDocument = {}  # type: ignore[typeddict-item]
    if "metadata" in data:
        import aws_sdk_bedrock_agent.types.document_metadata

        out["metadata"] = (
            aws_sdk_bedrock_agent.types.document_metadata.deserialize_json(
                data["metadata"]
            )
        )
    if "content" in data:
        import aws_sdk_bedrock_agent.types.document_content

        out["content"] = aws_sdk_bedrock_agent.types.document_content.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("KnowledgeBaseDocument.content required")
    return out
