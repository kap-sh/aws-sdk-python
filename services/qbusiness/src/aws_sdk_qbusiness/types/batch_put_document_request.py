"""Generated from Smithy shape ``com.amazonaws.qbusiness#BatchPutDocumentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.documents
    import aws_sdk_qbusiness.types.execution_id
    import aws_sdk_qbusiness.types.index_id
    import aws_sdk_qbusiness.types.role_arn


class BatchPutDocumentRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application.</p>"""
    index_id: "aws_sdk_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the Amazon Q Business index to add the documents to. </p>"""
    documents: "aws_sdk_qbusiness.types.documents.Documents"
    """<p>One or more documents to add to the index.</p> <important> <p>Ensure that the name of your document doesn't contain any confidential information. Amazon Q Business returns document names in chat responses and citations when relevant.</p> </important>"""
    role_arn: NotRequired["aws_sdk_qbusiness.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to access your S3 bucket.</p>"""
    data_source_sync_id: NotRequired["aws_sdk_qbusiness.types.execution_id.ExecutionId"]
    """<p>The identifier of the data source sync during which the documents were added.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutDocumentRequest) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.documents

    out["documents"] = aws_sdk_qbusiness.types.documents.serialize_json(
        value["documents"]
    )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "data_source_sync_id" in value:
        out["dataSourceSyncId"] = value["data_source_sync_id"]
    return out


def deserialize_json(data: dict) -> BatchPutDocumentRequest:
    out: BatchPutDocumentRequest = {}  # type: ignore[typeddict-item]
    if "documents" in data:
        import aws_sdk_qbusiness.types.documents

        out["documents"] = aws_sdk_qbusiness.types.documents.deserialize_json(
            data["documents"]
        )
    else:
        raise DeserializationError("BatchPutDocumentRequest.documents required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "dataSourceSyncId" in data:
        out["data_source_sync_id"] = data["dataSourceSyncId"]
    return out
