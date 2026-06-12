"""Generated from Smithy shape ``com.amazonaws.kendra#BatchPutDocumentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.batch_put_document_response_failed_documents


class BatchPutDocumentResponse(TypedDict):
    failed_documents: NotRequired[
        "aws_sdk_kendra.types.batch_put_document_response_failed_documents.BatchPutDocumentResponseFailedDocuments"
    ]
    """<p>A list of documents that were not added to the index because the document failed a validation check. Each document contains an error message that indicates why the document couldn't be added to the index.</p> <p>If there was an error adding a document to an index the error is reported in your Amazon Web Services CloudWatch log. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/cloudwatch-logs.html\">Monitoring Amazon Kendra with Amazon CloudWatch logs</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchPutDocumentResponse) -> dict:
    out: dict = {}
    if "failed_documents" in value:
        import aws_sdk_kendra.types.batch_put_document_response_failed_documents

        out["FailedDocuments"] = (
            aws_sdk_kendra.types.batch_put_document_response_failed_documents.serialize_aws_json_1_1(
                value["failed_documents"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchPutDocumentResponse:
    out: BatchPutDocumentResponse = {}  # type: ignore[typeddict-item]
    if "FailedDocuments" in data:
        import aws_sdk_kendra.types.batch_put_document_response_failed_documents

        out["failed_documents"] = (
            aws_sdk_kendra.types.batch_put_document_response_failed_documents.deserialize_aws_json_1_1(
                data["FailedDocuments"]
            )
        )
    return out
