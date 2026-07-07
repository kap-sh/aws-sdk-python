"""Generated from Smithy shape ``com.amazonaws.kendra#BatchDeleteDocumentResponseFailedDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_id
    import aws_sdk_kendra.types.document_id
    import aws_sdk_kendra.types.error_code
    import aws_sdk_kendra.types.error_message


class BatchDeleteDocumentResponseFailedDocument(TypedDict, closed=True):
    id: NotRequired["aws_sdk_kendra.types.document_id.DocumentId"]
    """<p>The identifier of the document that couldn't be removed from the index.</p>"""
    data_source_id: NotRequired["aws_sdk_kendra.types.data_source_id.DataSourceId"]
    """<p> The identifier of the data source connector that the document belongs to. </p>"""
    error_code: NotRequired["aws_sdk_kendra.types.error_code.ErrorCode"]
    """<p>The error code for why the document couldn't be removed from the index.</p>"""
    error_message: NotRequired["aws_sdk_kendra.types.error_message.ErrorMessage"]
    """<p>An explanation for why the document couldn't be removed from the index.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteDocumentResponseFailedDocument) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
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


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteDocumentResponseFailedDocument:
    out: BatchDeleteDocumentResponseFailedDocument = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
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
