"""Generated from Smithy shape ``com.amazonaws.kendra#BatchGetDocumentStatusResponseErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.batch_get_document_status_response_error

BatchGetDocumentStatusResponseErrors: TypeAlias = list[
    "aws_sdk_kendra.types.batch_get_document_status_response_error.BatchGetDocumentStatusResponseError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDocumentStatusResponseErrors) -> list:
    import aws_sdk_kendra.types.batch_get_document_status_response_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.batch_get_document_status_response_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchGetDocumentStatusResponseErrors:
    import aws_sdk_kendra.types.batch_get_document_status_response_error

    out: BatchGetDocumentStatusResponseErrors = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.batch_get_document_status_response_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
