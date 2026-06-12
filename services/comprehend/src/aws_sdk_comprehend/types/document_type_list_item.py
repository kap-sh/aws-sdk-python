"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentTypeListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_type
    import aws_sdk_comprehend.types.integer


class DocumentTypeListItem(TypedDict):
    page: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>Page number.</p>"""
    type: NotRequired["aws_sdk_comprehend.types.document_type.DocumentType"]
    """<p>Document type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentTypeListItem) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    if "type" in value:
        import aws_sdk_comprehend.types.document_type

        out["Type"] = aws_sdk_comprehend.types.document_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentTypeListItem:
    out: DocumentTypeListItem = {}  # type: ignore[typeddict-item]
    if "Page" in data:
        out["page"] = data["Page"]
    if "Type" in data:
        import aws_sdk_comprehend.types.document_type

        out["type"] = aws_sdk_comprehend.types.document_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
