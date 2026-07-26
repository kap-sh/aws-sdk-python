"""Generated from Smithy shape ``com.amazonaws.batch#FrontOfQueueDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.front_of_queue_job_summary_list
    import capo_batch.types.long


class FrontOfQueueDetail(TypedDict, closed=True):
    jobs: NotRequired[
        "capo_batch.types.front_of_queue_job_summary_list.FrontOfQueueJobSummaryList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the first 100 <code>RUNNABLE</code> jobs in a named job queue. For first-in-first-out (FIFO) job queues, jobs are ordered based on their submission time. For fair-share scheduling (FSS) job queues, jobs are ordered based on their job priority and share usage.</p>"""
    last_updated_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when each of the first 100 <code>RUNNABLE</code> jobs were last updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrontOfQueueDetail) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_batch.types.front_of_queue_job_summary_list

        out["jobs"] = capo_batch.types.front_of_queue_job_summary_list.serialize_json(
            value["jobs"]
        )
    if "last_updated_at" in value:
        out["lastUpdatedAt"] = value["last_updated_at"]
    return out


def deserialize_json(data: dict) -> FrontOfQueueDetail:
    out: FrontOfQueueDetail = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import capo_batch.types.front_of_queue_job_summary_list

        out["jobs"] = capo_batch.types.front_of_queue_job_summary_list.deserialize_json(
            data["jobs"]
        )
    if "lastUpdatedAt" in data:
        out["last_updated_at"] = data["lastUpdatedAt"]
    return out
