"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#GetPendingJobExecutionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_jobs_data_plane.types.job_execution_summary_list


class GetPendingJobExecutionsResponse(TypedDict):
    in_progress_jobs: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.job_execution_summary_list.JobExecutionSummaryList"
    ]
    """<p>A list of JobExecutionSummary objects with status IN_PROGRESS.</p>"""
    queued_jobs: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.job_execution_summary_list.JobExecutionSummaryList"
    ]
    """<p>A list of JobExecutionSummary objects with status QUEUED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPendingJobExecutionsResponse) -> dict:
    out: dict = {}
    if "in_progress_jobs" in value:
        import aws_sdk_iot_jobs_data_plane.types.job_execution_summary_list

        out["inProgressJobs"] = (
            aws_sdk_iot_jobs_data_plane.types.job_execution_summary_list.serialize_json(
                value["in_progress_jobs"]
            )
        )
    if "queued_jobs" in value:
        import aws_sdk_iot_jobs_data_plane.types.job_execution_summary_list

        out["queuedJobs"] = (
            aws_sdk_iot_jobs_data_plane.types.job_execution_summary_list.serialize_json(
                value["queued_jobs"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPendingJobExecutionsResponse:
    out: GetPendingJobExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "inProgressJobs" in data:
        import aws_sdk_iot_jobs_data_plane.types.job_execution_summary_list

        out["in_progress_jobs"] = (
            aws_sdk_iot_jobs_data_plane.types.job_execution_summary_list.deserialize_json(
                data["inProgressJobs"]
            )
        )
    if "queuedJobs" in data:
        import aws_sdk_iot_jobs_data_plane.types.job_execution_summary_list

        out["queued_jobs"] = (
            aws_sdk_iot_jobs_data_plane.types.job_execution_summary_list.deserialize_json(
                data["queuedJobs"]
            )
        )
    return out
