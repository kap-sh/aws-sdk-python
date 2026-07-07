"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceSyncJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_sync_job_metrics
    import aws_sdk_kendra.types.data_source_sync_job_status
    import aws_sdk_kendra.types.error_code
    import aws_sdk_kendra.types.error_message
    import aws_sdk_kendra.types.string
    import aws_sdk_kendra.types.timestamp


class DataSourceSyncJob(TypedDict, closed=True):
    execution_id: NotRequired["aws_sdk_kendra.types.string.String"]
    """<p>A identifier for the synchronization job.</p>"""
    start_time: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the synchronization job started.</p>"""
    end_time: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the synchronization job completed.</p>"""
    status: NotRequired[
        "aws_sdk_kendra.types.data_source_sync_job_status.DataSourceSyncJobStatus"
    ]
    """<p>The execution status of the synchronization job. When the <code>Status</code> field is set to <code>SUCCEEDED</code>, the synchronization job is done. If the status code is set to <code>FAILED</code>, the <code>ErrorCode</code> and <code>ErrorMessage</code> fields give you the reason for the failure.</p>"""
    error_message: NotRequired["aws_sdk_kendra.types.error_message.ErrorMessage"]
    """<p>If the <code>Status</code> field is set to <code>ERROR</code>, the <code>ErrorMessage</code> field contains a description of the error that caused the synchronization to fail.</p>"""
    error_code: NotRequired["aws_sdk_kendra.types.error_code.ErrorCode"]
    """<p>If the <code>Status</code> field is set to <code>FAILED</code>, the <code>ErrorCode</code> field indicates the reason the synchronization failed.</p>"""
    data_source_error_code: NotRequired["aws_sdk_kendra.types.string.String"]
    """<p>If the reason that the synchronization failed is due to an error with the underlying data source, this field contains a code that identifies the error.</p>"""
    metrics: NotRequired[
        "aws_sdk_kendra.types.data_source_sync_job_metrics.DataSourceSyncJobMetrics"
    ]
    """<p>Maps a batch delete document request to a specific data source sync job. This is optional and should only be supplied when documents are deleted by a data source connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceSyncJob) -> dict:
    out: dict = {}
    if "execution_id" in value:
        out["ExecutionId"] = value["execution_id"]
    if "start_time" in value:
        import aws_sdk_kendra.types.timestamp

        out["StartTime"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_kendra.types.timestamp

        out["EndTime"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "status" in value:
        import aws_sdk_kendra.types.data_source_sync_job_status

        out["Status"] = (
            aws_sdk_kendra.types.data_source_sync_job_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_code" in value:
        import aws_sdk_kendra.types.error_code

        out["ErrorCode"] = aws_sdk_kendra.types.error_code.serialize_aws_json_1_1(
            value["error_code"]
        )
    if "data_source_error_code" in value:
        out["DataSourceErrorCode"] = value["data_source_error_code"]
    if "metrics" in value:
        import aws_sdk_kendra.types.data_source_sync_job_metrics

        out["Metrics"] = (
            aws_sdk_kendra.types.data_source_sync_job_metrics.serialize_aws_json_1_1(
                value["metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSourceSyncJob:
    out: DataSourceSyncJob = {}  # type: ignore[typeddict-item]
    if "ExecutionId" in data:
        out["execution_id"] = data["ExecutionId"]
    if "StartTime" in data:
        import aws_sdk_kendra.types.timestamp

        out["start_time"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_kendra.types.timestamp

        out["end_time"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "Status" in data:
        import aws_sdk_kendra.types.data_source_sync_job_status

        out["status"] = (
            aws_sdk_kendra.types.data_source_sync_job_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "ErrorCode" in data:
        import aws_sdk_kendra.types.error_code

        out["error_code"] = aws_sdk_kendra.types.error_code.deserialize_aws_json_1_1(
            data["ErrorCode"]
        )
    if "DataSourceErrorCode" in data:
        out["data_source_error_code"] = data["DataSourceErrorCode"]
    if "Metrics" in data:
        import aws_sdk_kendra.types.data_source_sync_job_metrics

        out["metrics"] = (
            aws_sdk_kendra.types.data_source_sync_job_metrics.deserialize_aws_json_1_1(
                data["Metrics"]
            )
        )
    return out
