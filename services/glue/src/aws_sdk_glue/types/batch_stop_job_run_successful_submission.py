"""Generated from Smithy shape ``com.amazonaws.glue#BatchStopJobRunSuccessfulSubmission``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.id_string
    import aws_sdk_glue.types.name_string


class BatchStopJobRunSuccessfulSubmission(TypedDict):
    job_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the job definition used in the job run that was stopped.</p>"""
    job_run_id: NotRequired["aws_sdk_glue.types.id_string.IdString"]
    """<p>The <code>JobRunId</code> of the job run that was stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchStopJobRunSuccessfulSubmission) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_run_id" in value:
        out["JobRunId"] = value["job_run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchStopJobRunSuccessfulSubmission:
    out: BatchStopJobRunSuccessfulSubmission = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobRunId" in data:
        out["job_run_id"] = data["JobRunId"]
    return out
