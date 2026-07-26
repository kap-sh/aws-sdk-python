"""Generated from Smithy shape ``com.amazonaws.batch#UpdateServiceJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer
    import capo_batch.types.string


class UpdateServiceJobRequest(TypedDict, closed=True):
    job_id: NotRequired["capo_batch.types.string.String"]
    """<p>The Batch job ID of the job to update.</p>"""
    scheduling_priority: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The scheduling priority for the job. This only affects jobs in job queues with a quota-share or fair-share scheduling policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority within a share.</p> <p>The minimum supported value is 0 and the maximum supported value is 9999.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceJobRequest) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "scheduling_priority" in value:
        out["schedulingPriority"] = value["scheduling_priority"]
    return out


def deserialize_json(data: dict) -> UpdateServiceJobRequest:
    out: UpdateServiceJobRequest = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "schedulingPriority" in data:
        out["scheduling_priority"] = data["schedulingPriority"]
    return out
