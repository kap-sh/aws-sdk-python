"""Generated from Smithy shape ``com.amazonaws.qbusiness#BatchDeleteDocumentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.failed_documents


class BatchDeleteDocumentResponse(TypedDict, closed=True):
    failed_documents: NotRequired[
        "capo_qbusiness.types.failed_documents.FailedDocuments"
    ]
    """<p>A list of documents that couldn't be removed from the Amazon Q Business index. Each entry contains an error message that indicates why the document couldn't be removed from the index. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDocumentResponse) -> dict:
    out: dict = {}
    if "failed_documents" in value:
        import capo_qbusiness.types.failed_documents

        out["failedDocuments"] = capo_qbusiness.types.failed_documents.serialize_json(
            value["failed_documents"]
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteDocumentResponse:
    out: BatchDeleteDocumentResponse = {}  # type: ignore[typeddict-item]
    if "failedDocuments" in data:
        import capo_qbusiness.types.failed_documents

        out["failed_documents"] = (
            capo_qbusiness.types.failed_documents.deserialize_json(
                data["failedDocuments"]
            )
        )
    return out
