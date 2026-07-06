"""Generated from Smithy shape ``com.amazonaws.kendra#BatchGetDocumentStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.batch_get_document_status_response_errors
    import aws_sdk_kendra.types.document_status_list


class BatchGetDocumentStatusResponse(TypedDict, closed=True):
    errors: NotRequired[
        "aws_sdk_kendra.types.batch_get_document_status_response_errors.BatchGetDocumentStatusResponseErrors"
    ]
    """<p>A list of documents that Amazon Kendra couldn't get the status for. The list includes the ID of the document and the reason that the status couldn't be found.</p>"""
    document_status_list: NotRequired[
        "aws_sdk_kendra.types.document_status_list.DocumentStatusList"
    ]
    """<p>The status of documents. The status indicates if the document is waiting to be indexed, is in the process of indexing, has completed indexing, or failed indexing. If a document failed indexing, the status provides the reason why.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDocumentStatusResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_kendra.types.batch_get_document_status_response_errors

        out["Errors"] = (
            aws_sdk_kendra.types.batch_get_document_status_response_errors.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    if "document_status_list" in value:
        import aws_sdk_kendra.types.document_status_list

        out["DocumentStatusList"] = (
            aws_sdk_kendra.types.document_status_list.serialize_aws_json_1_1(
                value["document_status_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDocumentStatusResponse:
    out: BatchGetDocumentStatusResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_kendra.types.batch_get_document_status_response_errors

        out["errors"] = (
            aws_sdk_kendra.types.batch_get_document_status_response_errors.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    if "DocumentStatusList" in data:
        import aws_sdk_kendra.types.document_status_list

        out["document_status_list"] = (
            aws_sdk_kendra.types.document_status_list.deserialize_aws_json_1_1(
                data["DocumentStatusList"]
            )
        )
    return out
