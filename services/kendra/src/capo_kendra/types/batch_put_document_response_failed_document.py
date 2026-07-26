"""Generated from Smithy shape ``com.amazonaws.kendra#BatchPutDocumentResponseFailedDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.data_source_id
    import capo_kendra.types.document_id
    import capo_kendra.types.error_code
    import capo_kendra.types.error_message


class BatchPutDocumentResponseFailedDocument(TypedDict, closed=True):
    id: NotRequired["capo_kendra.types.document_id.DocumentId"]
    """<p>The identifier of the document.</p>"""
    data_source_id: NotRequired["capo_kendra.types.data_source_id.DataSourceId"]
    """<p> The identifier of the data source connector that the failed document belongs to. </p>"""
    error_code: NotRequired["capo_kendra.types.error_code.ErrorCode"]
    """<p>The type of error that caused the document to fail to be indexed.</p>"""
    error_message: NotRequired["capo_kendra.types.error_message.ErrorMessage"]
    """<p>A description of the reason why the document could not be indexed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchPutDocumentResponseFailedDocument) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    if "error_code" in value:
        import capo_kendra.types.error_code

        out["ErrorCode"] = capo_kendra.types.error_code.serialize_aws_json_1_1(
            value["error_code"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchPutDocumentResponseFailedDocument:
    out: BatchPutDocumentResponseFailedDocument = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    if "ErrorCode" in data:
        import capo_kendra.types.error_code

        out["error_code"] = capo_kendra.types.error_code.deserialize_aws_json_1_1(
            data["ErrorCode"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
