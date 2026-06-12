"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#JobExecutionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_jobs_data_plane.types.job_execution_summary

JobExecutionSummaryList: TypeAlias = list[
    "aws_sdk_iot_jobs_data_plane.types.job_execution_summary.JobExecutionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobExecutionSummaryList) -> list:
    import aws_sdk_iot_jobs_data_plane.types.job_execution_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_jobs_data_plane.types.job_execution_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> JobExecutionSummaryList:
    import aws_sdk_iot_jobs_data_plane.types.job_execution_summary

    out: JobExecutionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_iot_jobs_data_plane.types.job_execution_summary.deserialize_json(
                item
            )
        )
    return out
