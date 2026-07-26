"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataSourceSyncJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.data_source_sync_job_metrics
    import capo_qbusiness.types.data_source_sync_job_status
    import capo_qbusiness.types.error_detail
    import capo_qbusiness.types.execution_id
    import capo_qbusiness.types.string
    import capo_qbusiness.types.timestamp


class DataSourceSyncJob(TypedDict, closed=True):
    execution_id: NotRequired["capo_qbusiness.types.execution_id.ExecutionId"]
    """<p>The identifier of a data source synchronization job.</p>"""
    start_time: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix time stamp when the data source synchronization job started.</p>"""
    end_time: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the synchronization job completed.</p>"""
    status: NotRequired[
        "capo_qbusiness.types.data_source_sync_job_status.DataSourceSyncJobStatus"
    ]
    """<p>The status of the synchronization job. When the <code>Status</code> field is set to <code>SUCCEEDED</code>, the synchronization job is done. If the status code is <code>FAILED</code>, the <code>ErrorCode</code> and <code>ErrorMessage</code> fields give you the reason for the failure.</p>"""
    error: NotRequired["capo_qbusiness.types.error_detail.ErrorDetail"]
    """<p>If the <code>Status</code> field is set to <code>FAILED</code>, the <code>ErrorCode</code> field indicates the reason the synchronization failed. </p>"""
    data_source_error_code: NotRequired["capo_qbusiness.types.string.String"]
    """<p>If the reason that the synchronization failed is due to an error with the underlying data source, this field contains a code that identifies the error.</p>"""
    metrics: NotRequired[
        "capo_qbusiness.types.data_source_sync_job_metrics.DataSourceSyncJobMetrics"
    ]
    """<p>Maps a batch delete document request to a specific data source sync job. This is optional and should only be supplied when documents are deleted by a data source connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceSyncJob) -> dict:
    out: dict = {}
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    if "start_time" in value:
        import capo_qbusiness.types.timestamp

        out["startTime"] = capo_qbusiness.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_qbusiness.types.timestamp

        out["endTime"] = capo_qbusiness.types.timestamp.serialize_json(
            value["end_time"]
        )
    if "status" in value:
        import capo_qbusiness.types.data_source_sync_job_status

        out["status"] = capo_qbusiness.types.data_source_sync_job_status.serialize_json(
            value["status"]
        )
    if "error" in value:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.serialize_json(value["error"])
    if "data_source_error_code" in value:
        out["dataSourceErrorCode"] = value["data_source_error_code"]
    if "metrics" in value:
        import capo_qbusiness.types.data_source_sync_job_metrics

        out["metrics"] = (
            capo_qbusiness.types.data_source_sync_job_metrics.serialize_json(
                value["metrics"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSourceSyncJob:
    out: DataSourceSyncJob = {}  # type: ignore[typeddict-item]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    if "startTime" in data:
        import capo_qbusiness.types.timestamp

        out["start_time"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import capo_qbusiness.types.timestamp

        out["end_time"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["endTime"]
        )
    if "status" in data:
        import capo_qbusiness.types.data_source_sync_job_status

        out["status"] = (
            capo_qbusiness.types.data_source_sync_job_status.deserialize_json(
                data["status"]
            )
        )
    if "error" in data:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.deserialize_json(data["error"])
    if "dataSourceErrorCode" in data:
        out["data_source_error_code"] = data["dataSourceErrorCode"]
    if "metrics" in data:
        import capo_qbusiness.types.data_source_sync_job_metrics

        out["metrics"] = (
            capo_qbusiness.types.data_source_sync_job_metrics.deserialize_json(
                data["metrics"]
            )
        )
    return out
