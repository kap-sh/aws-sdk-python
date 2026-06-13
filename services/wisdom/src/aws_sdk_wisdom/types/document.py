"""Generated from Smithy shape ``com.amazonaws.wisdom#Document``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.content_reference
    import aws_sdk_wisdom.types.document_text


class Document(TypedDict):
    content_reference: "aws_sdk_wisdom.types.content_reference.ContentReference"
    """<p>A reference to the content resource.</p>"""
    title: NotRequired["aws_sdk_wisdom.types.document_text.DocumentText"]
    """<p>The title of the document.</p>"""
    excerpt: NotRequired["aws_sdk_wisdom.types.document_text.DocumentText"]
    """<p>The excerpt from the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Document) -> dict:
    out: dict = {}
    import aws_sdk_wisdom.types.content_reference

    out["contentReference"] = aws_sdk_wisdom.types.content_reference.serialize_json(
        value["content_reference"]
    )
    if "title" in value:
        import aws_sdk_wisdom.types.document_text

        out["title"] = aws_sdk_wisdom.types.document_text.serialize_json(value["title"])
    if "excerpt" in value:
        import aws_sdk_wisdom.types.document_text

        out["excerpt"] = aws_sdk_wisdom.types.document_text.serialize_json(
            value["excerpt"]
        )
    return out


def deserialize_json(data: dict) -> Document:
    out: Document = {}  # type: ignore[typeddict-item]
    if "contentReference" in data:
        import aws_sdk_wisdom.types.content_reference

        out["content_reference"] = (
            aws_sdk_wisdom.types.content_reference.deserialize_json(
                data["contentReference"]
            )
        )
    else:
        raise DeserializationError("Document.content_reference required")
    if "title" in data:
        import aws_sdk_wisdom.types.document_text

        out["title"] = aws_sdk_wisdom.types.document_text.deserialize_json(
            data["title"]
        )
    if "excerpt" in data:
        import aws_sdk_wisdom.types.document_text

        out["excerpt"] = aws_sdk_wisdom.types.document_text.deserialize_json(
            data["excerpt"]
        )
    return out
