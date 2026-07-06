"""Generated from Smithy shape ``com.amazonaws.iot#JobExecutionSummaryForThing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.job_execution_summary
    import aws_sdk_iot.types.job_id


class JobExecutionSummaryForThing(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_iot.types.job_id.JobId"]
    """<p>The unique identifier you assigned to this job when it was created.</p>"""
    job_execution_summary: NotRequired[
        "aws_sdk_iot.types.job_execution_summary.JobExecutionSummary"
    ]
    """<p>Contains a subset of information about a job execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobExecutionSummaryForThing) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_execution_summary" in value:
        import aws_sdk_iot.types.job_execution_summary

        out["jobExecutionSummary"] = (
            aws_sdk_iot.types.job_execution_summary.serialize_json(
                value["job_execution_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobExecutionSummaryForThing:
    out: JobExecutionSummaryForThing = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "jobExecutionSummary" in data:
        import aws_sdk_iot.types.job_execution_summary

        out["job_execution_summary"] = (
            aws_sdk_iot.types.job_execution_summary.deserialize_json(
                data["jobExecutionSummary"]
            )
        )
    return out
