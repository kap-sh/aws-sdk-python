"""Generated from Smithy shape ``com.amazonaws.kendra#BatchDeleteDocumentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.batch_delete_document_response_failed_documents


class BatchDeleteDocumentResponse(TypedDict):
    failed_documents: NotRequired[
        "aws_sdk_kendra.types.batch_delete_document_response_failed_documents.BatchDeleteDocumentResponseFailedDocuments"
    ]
    """<p>A list of documents that could not be removed from the index. Each entry contains an error message that indicates why the document couldn't be removed from the index.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteDocumentResponse) -> dict:
    out: dict = {}
    if "failed_documents" in value:
        import aws_sdk_kendra.types.batch_delete_document_response_failed_documents

        out["FailedDocuments"] = (
            aws_sdk_kendra.types.batch_delete_document_response_failed_documents.serialize_aws_json_1_1(
                value["failed_documents"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteDocumentResponse:
    out: BatchDeleteDocumentResponse = {}  # type: ignore[typeddict-item]
    if "FailedDocuments" in data:
        import aws_sdk_kendra.types.batch_delete_document_response_failed_documents

        out["failed_documents"] = (
            aws_sdk_kendra.types.batch_delete_document_response_failed_documents.deserialize_aws_json_1_1(
                data["FailedDocuments"]
            )
        )
    return out
