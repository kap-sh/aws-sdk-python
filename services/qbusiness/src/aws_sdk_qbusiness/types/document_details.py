"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.document_id
    import aws_sdk_qbusiness.types.document_status
    import aws_sdk_qbusiness.types.error_detail
    import aws_sdk_qbusiness.types.timestamp


class DocumentDetails(TypedDict, closed=True):
    document_id: NotRequired["aws_sdk_qbusiness.types.document_id.DocumentId"]
    """<p>The identifier of the document.</p>"""
    status: NotRequired["aws_sdk_qbusiness.types.document_status.DocumentStatus"]
    """<p>The current status of the document.</p>"""
    error: NotRequired["aws_sdk_qbusiness.types.error_detail.ErrorDetail"]
    """<p>An error message associated with the document.</p>"""
    created_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp for when the document was created.</p>"""
    updated_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp for when the document was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentDetails) -> dict:
    out: dict = {}
    if "document_id" in value:
        out["documentId"] = value["document_id"]
    if "status" in value:
        import aws_sdk_qbusiness.types.document_status

        out["status"] = aws_sdk_qbusiness.types.document_status.serialize_json(
            value["status"]
        )
    if "error" in value:
        import aws_sdk_qbusiness.types.error_detail

        out["error"] = aws_sdk_qbusiness.types.error_detail.serialize_json(
            value["error"]
        )
    if "created_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["createdAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["updatedAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> DocumentDetails:
    out: DocumentDetails = {}  # type: ignore[typeddict-item]
    if "documentId" in data:
        out["document_id"] = data["documentId"]
    if "status" in data:
        import aws_sdk_qbusiness.types.document_status

        out["status"] = aws_sdk_qbusiness.types.document_status.deserialize_json(
            data["status"]
        )
    if "error" in data:
        import aws_sdk_qbusiness.types.error_detail

        out["error"] = aws_sdk_qbusiness.types.error_detail.deserialize_json(
            data["error"]
        )
    if "createdAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["created_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["updated_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
