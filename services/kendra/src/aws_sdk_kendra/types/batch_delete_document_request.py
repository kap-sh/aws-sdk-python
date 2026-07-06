"""Generated from Smithy shape ``com.amazonaws.kendra#BatchDeleteDocumentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_sync_job_metric_target
    import aws_sdk_kendra.types.document_id_list
    import aws_sdk_kendra.types.index_id


class BatchDeleteDocumentRequest(TypedDict, closed=True):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index that contains the documents to delete.</p>"""
    document_id_list: "aws_sdk_kendra.types.document_id_list.DocumentIdList"
    """<p>One or more identifiers for documents to delete from the index.</p>"""
    data_source_sync_job_metric_target: NotRequired[
        "aws_sdk_kendra.types.data_source_sync_job_metric_target.DataSourceSyncJobMetricTarget"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteDocumentRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    import aws_sdk_kendra.types.document_id_list

    out["DocumentIdList"] = (
        aws_sdk_kendra.types.document_id_list.serialize_aws_json_1_1(
            value["document_id_list"]
        )
    )
    if "data_source_sync_job_metric_target" in value:
        import aws_sdk_kendra.types.data_source_sync_job_metric_target

        out["DataSourceSyncJobMetricTarget"] = (
            aws_sdk_kendra.types.data_source_sync_job_metric_target.serialize_aws_json_1_1(
                value["data_source_sync_job_metric_target"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteDocumentRequest:
    out: BatchDeleteDocumentRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("BatchDeleteDocumentRequest.index_id required")
    if "DocumentIdList" in data:
        import aws_sdk_kendra.types.document_id_list

        out["document_id_list"] = (
            aws_sdk_kendra.types.document_id_list.deserialize_aws_json_1_1(
                data["DocumentIdList"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteDocumentRequest.document_id_list required"
        )
    if "DataSourceSyncJobMetricTarget" in data:
        import aws_sdk_kendra.types.data_source_sync_job_metric_target

        out["data_source_sync_job_metric_target"] = (
            aws_sdk_kendra.types.data_source_sync_job_metric_target.deserialize_aws_json_1_1(
                data["DataSourceSyncJobMetricTarget"]
            )
        )
    return out
