"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDashboardSnapshotJobResultResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.non_empty_string
    import aws_sdk_quicksight.types.snapshot_job_error_info
    import aws_sdk_quicksight.types.snapshot_job_result
    import aws_sdk_quicksight.types.snapshot_job_status
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.timestamp


class DescribeDashboardSnapshotJobResultResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the snapshot job. The job ARN is generated when you start a new job with a <code>StartDashboardSnapshotJob</code> API call.</p>"""
    job_status: NotRequired[
        "aws_sdk_quicksight.types.snapshot_job_status.SnapshotJobStatus"
    ]
    """<p>Indicates the status of a job after it has reached a terminal state. A finished snapshot job will retuen a <code>COMPLETED</code> or <code>FAILED</code> status.</p>"""
    created_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The time that a snapshot job was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The time that a snapshot job status was last updated.</p>"""
    result: NotRequired[
        "aws_sdk_quicksight.types.snapshot_job_result.SnapshotJobResult"
    ]
    """<p>The result of the snapshot job. Jobs that have successfully completed will return the S3Uri where they are located. Jobs that have failedwill return information on the error that caused the job to fail.</p>"""
    error_info: NotRequired[
        "aws_sdk_quicksight.types.snapshot_job_error_info.SnapshotJobErrorInfo"
    ]
    """<p>Displays information for the error that caused a job to fail.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardSnapshotJobResultResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "job_status" in value:
        import aws_sdk_quicksight.types.snapshot_job_status

        out["JobStatus"] = aws_sdk_quicksight.types.snapshot_job_status.serialize_json(
            value["job_status"]
        )
    if "created_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["LastUpdatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "result" in value:
        import aws_sdk_quicksight.types.snapshot_job_result

        out["Result"] = aws_sdk_quicksight.types.snapshot_job_result.serialize_json(
            value["result"]
        )
    if "error_info" in value:
        import aws_sdk_quicksight.types.snapshot_job_error_info

        out["ErrorInfo"] = (
            aws_sdk_quicksight.types.snapshot_job_error_info.serialize_json(
                value["error_info"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeDashboardSnapshotJobResultResponse:
    out: DescribeDashboardSnapshotJobResultResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "JobStatus" in data:
        import aws_sdk_quicksight.types.snapshot_job_status

        out["job_status"] = (
            aws_sdk_quicksight.types.snapshot_job_status.deserialize_json(
                data["JobStatus"]
            )
        )
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["last_updated_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "Result" in data:
        import aws_sdk_quicksight.types.snapshot_job_result

        out["result"] = aws_sdk_quicksight.types.snapshot_job_result.deserialize_json(
            data["Result"]
        )
    if "ErrorInfo" in data:
        import aws_sdk_quicksight.types.snapshot_job_error_info

        out["error_info"] = (
            aws_sdk_quicksight.types.snapshot_job_error_info.deserialize_json(
                data["ErrorInfo"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
