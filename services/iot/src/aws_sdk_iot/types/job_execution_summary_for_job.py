"""Generated from Smithy shape ``com.amazonaws.iot#JobExecutionSummaryForJob``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.job_execution_summary
    import aws_sdk_iot.types.thing_arn


class JobExecutionSummaryForJob(TypedDict):
    thing_arn: NotRequired["aws_sdk_iot.types.thing_arn.ThingArn"]
    """<p>The ARN of the thing on which the job execution is running.</p>"""
    job_execution_summary: NotRequired[
        "aws_sdk_iot.types.job_execution_summary.JobExecutionSummary"
    ]
    """<p>Contains a subset of information about a job execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobExecutionSummaryForJob) -> dict:
    out: dict = {}
    if "thing_arn" in value:
        out["thingArn"] = value["thing_arn"]
    if "job_execution_summary" in value:
        import aws_sdk_iot.types.job_execution_summary

        out["jobExecutionSummary"] = (
            aws_sdk_iot.types.job_execution_summary.serialize_json(
                value["job_execution_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobExecutionSummaryForJob:
    out: JobExecutionSummaryForJob = {}  # type: ignore[typeddict-item]
    if "thingArn" in data:
        out["thing_arn"] = data["thingArn"]
    if "jobExecutionSummary" in data:
        import aws_sdk_iot.types.job_execution_summary

        out["job_execution_summary"] = (
            aws_sdk_iot.types.job_execution_summary.deserialize_json(
                data["jobExecutionSummary"]
            )
        )
    return out
