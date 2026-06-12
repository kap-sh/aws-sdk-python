"""Generated from Smithy shape ``com.amazonaws.batch#TerminateJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class TerminateJobRequest(TypedDict):
    job_id: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Batch job ID of the job to terminate.</p>"""
    reason: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>A message to attach to the job that explains the reason for canceling it. This message is returned by future <a>DescribeJobs</a> operations on the job. It is also recorded in the Batch activity logs.</p> <p>This parameter has as limit of 1024 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerminateJobRequest) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> TerminateJobRequest:
    out: TerminateJobRequest = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
