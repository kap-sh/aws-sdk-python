"""Generated from Smithy shape ``com.amazonaws.kendra#BatchDeleteDocumentResponseFailedDocuments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.batch_delete_document_response_failed_document

BatchDeleteDocumentResponseFailedDocuments: TypeAlias = list[
    "capo_kendra.types.batch_delete_document_response_failed_document.BatchDeleteDocumentResponseFailedDocument"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteDocumentResponseFailedDocuments) -> list:
    import capo_kendra.types.batch_delete_document_response_failed_document

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.batch_delete_document_response_failed_document.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchDeleteDocumentResponseFailedDocuments:
    import capo_kendra.types.batch_delete_document_response_failed_document

    out: BatchDeleteDocumentResponseFailedDocuments = []
    for item in data:
        out.append(
            capo_kendra.types.batch_delete_document_response_failed_document.deserialize_aws_json_1_1(
                item
            )
        )
    return out
