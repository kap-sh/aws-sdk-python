"""Generated from Smithy shape ``com.amazonaws.kendra#BatchPutDocumentResponseFailedDocuments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.batch_put_document_response_failed_document

BatchPutDocumentResponseFailedDocuments: TypeAlias = list[
    "aws_sdk_kendra.types.batch_put_document_response_failed_document.BatchPutDocumentResponseFailedDocument"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchPutDocumentResponseFailedDocuments) -> list:
    import aws_sdk_kendra.types.batch_put_document_response_failed_document

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.batch_put_document_response_failed_document.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchPutDocumentResponseFailedDocuments:
    import aws_sdk_kendra.types.batch_put_document_response_failed_document

    out: BatchPutDocumentResponseFailedDocuments = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.batch_put_document_response_failed_document.deserialize_aws_json_1_1(
                item
            )
        )
    return out
