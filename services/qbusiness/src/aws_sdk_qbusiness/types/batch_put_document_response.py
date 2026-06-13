"""Generated from Smithy shape ``com.amazonaws.qbusiness#BatchPutDocumentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.failed_documents


class BatchPutDocumentResponse(TypedDict):
    failed_documents: NotRequired[
        "aws_sdk_qbusiness.types.failed_documents.FailedDocuments"
    ]
    """<p> A list of documents that were not added to the Amazon Q Business index because the document failed a validation check. Each document contains an error message that indicates why the document couldn't be added to the index. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutDocumentResponse) -> dict:
    out: dict = {}
    if "failed_documents" in value:
        import aws_sdk_qbusiness.types.failed_documents

        out["failedDocuments"] = (
            aws_sdk_qbusiness.types.failed_documents.serialize_json(
                value["failed_documents"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchPutDocumentResponse:
    out: BatchPutDocumentResponse = {}  # type: ignore[typeddict-item]
    if "failedDocuments" in data:
        import aws_sdk_qbusiness.types.failed_documents

        out["failed_documents"] = (
            aws_sdk_qbusiness.types.failed_documents.deserialize_json(
                data["failedDocuments"]
            )
        )
    return out
