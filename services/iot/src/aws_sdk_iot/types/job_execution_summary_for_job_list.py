"""Generated from Smithy shape ``com.amazonaws.iot#JobExecutionSummaryForJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.job_execution_summary_for_job

JobExecutionSummaryForJobList: TypeAlias = list[
    "aws_sdk_iot.types.job_execution_summary_for_job.JobExecutionSummaryForJob"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobExecutionSummaryForJobList) -> list:
    import aws_sdk_iot.types.job_execution_summary_for_job

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.job_execution_summary_for_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobExecutionSummaryForJobList:
    import aws_sdk_iot.types.job_execution_summary_for_job

    out: JobExecutionSummaryForJobList = []
    for item in data:
        out.append(
            aws_sdk_iot.types.job_execution_summary_for_job.deserialize_json(item)
        )
    return out
