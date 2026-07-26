"""Generated from Smithy shape ``com.amazonaws.batch#CancelJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string


class CancelJobRequest(TypedDict, closed=True):
    job_id: NotRequired["capo_batch.types.string.String"]
    """<p>The Batch job ID of the job to cancel.</p>"""
    reason: NotRequired["capo_batch.types.string.String"]
    """<p>A message to attach to the job that explains the reason for canceling it. This message is returned by future <a>DescribeJobs</a> operations on the job. It is also recorded in the Batch activity logs.</p> <p>This parameter has as limit of 1024 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobRequest) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> CancelJobRequest:
    out: CancelJobRequest = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
