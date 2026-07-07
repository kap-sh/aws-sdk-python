"""Generated from Smithy shape ``com.amazonaws.kendra#BatchGetDocumentStatusResponseError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_id
    import aws_sdk_kendra.types.document_id
    import aws_sdk_kendra.types.error_code
    import aws_sdk_kendra.types.error_message


class BatchGetDocumentStatusResponseError(TypedDict, closed=True):
    document_id: NotRequired["aws_sdk_kendra.types.document_id.DocumentId"]
    """<p>The identifier of the document whose status could not be retrieved.</p>"""
    data_source_id: NotRequired["aws_sdk_kendra.types.data_source_id.DataSourceId"]
    """<p> The identifier of the data source connector that the failed document belongs to. </p>"""
    error_code: NotRequired["aws_sdk_kendra.types.error_code.ErrorCode"]
    """<p>Indicates the source of the error.</p>"""
    error_message: NotRequired["aws_sdk_kendra.types.error_message.ErrorMessage"]
    """<p>States that the API could not get the status of a document. This could be because the request is not valid or there is a system error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDocumentStatusResponseError) -> dict:
    out: dict = {}
    if "document_id" in value:
        out["DocumentId"] = value["document_id"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    if "error_code" in value:
        import aws_sdk_kendra.types.error_code

        out["ErrorCode"] = aws_sdk_kendra.types.error_code.serialize_aws_json_1_1(
            value["error_code"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDocumentStatusResponseError:
    out: BatchGetDocumentStatusResponseError = {}  # type: ignore[typeddict-item]
    if "DocumentId" in data:
        out["document_id"] = data["DocumentId"]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    if "ErrorCode" in data:
        import aws_sdk_kendra.types.error_code

        out["error_code"] = aws_sdk_kendra.types.error_code.deserialize_aws_json_1_1(
            data["ErrorCode"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
