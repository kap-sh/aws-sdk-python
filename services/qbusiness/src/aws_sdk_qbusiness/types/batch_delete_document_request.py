"""Generated from Smithy shape ``com.amazonaws.qbusiness#BatchDeleteDocumentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.delete_documents
    import aws_sdk_qbusiness.types.execution_id
    import aws_sdk_qbusiness.types.index_id


class BatchDeleteDocumentRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application.</p>"""
    index_id: "aws_sdk_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the Amazon Q Business index that contains the documents to delete.</p>"""
    documents: "aws_sdk_qbusiness.types.delete_documents.DeleteDocuments"
    """<p>Documents deleted from the Amazon Q Business index.</p>"""
    data_source_sync_id: NotRequired["aws_sdk_qbusiness.types.execution_id.ExecutionId"]
    """<p>The identifier of the data source sync during which the documents were deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDocumentRequest) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.delete_documents

    out["documents"] = aws_sdk_qbusiness.types.delete_documents.serialize_json(
        value["documents"]
    )
    if "data_source_sync_id" in value:
        out["dataSourceSyncId"] = value["data_source_sync_id"]
    return out


def deserialize_json(data: dict) -> BatchDeleteDocumentRequest:
    out: BatchDeleteDocumentRequest = {}  # type: ignore[typeddict-item]
    if "documents" in data:
        import aws_sdk_qbusiness.types.delete_documents

        out["documents"] = aws_sdk_qbusiness.types.delete_documents.deserialize_json(
            data["documents"]
        )
    else:
        raise DeserializationError("BatchDeleteDocumentRequest.documents required")
    if "dataSourceSyncId" in data:
        out["data_source_sync_id"] = data["dataSourceSyncId"]
    return out
