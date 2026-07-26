"""Generated from Smithy shape ``com.amazonaws.batch#GetJobQueueSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.front_of_queue_detail
    import capo_batch.types.front_of_quota_shares_detail
    import capo_batch.types.queue_snapshot_utilization_detail


class GetJobQueueSnapshotResponse(TypedDict, closed=True):
    front_of_queue: NotRequired[
        "capo_batch.types.front_of_queue_detail.FrontOfQueueDetail"
    ]
    """<p>The list of the first 100 <code>RUNNABLE</code> jobs in each job queue. For first-in-first-out (FIFO) job queues, jobs are ordered based on their submission time. For job queues with an attached fair-share scheduling (FSS) or quota-share policy, jobs are ordered based on their job priority and share usage.</p>"""
    front_of_quota_shares: NotRequired[
        "capo_batch.types.front_of_quota_shares_detail.FrontOfQuotaSharesDetail"
    ]
    """<p>The first <code>RUNNABLE</code> job in each quota share. Jobs are ordered based on their job priority and share usage.</p>"""
    queue_utilization: NotRequired[
        "capo_batch.types.queue_snapshot_utilization_detail.QueueSnapshotUtilizationDetail"
    ]
    """<p>The job queue's capacity utilization, including total usage and breakdown per given share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobQueueSnapshotResponse) -> dict:
    out: dict = {}
    if "front_of_queue" in value:
        import capo_batch.types.front_of_queue_detail

        out["frontOfQueue"] = capo_batch.types.front_of_queue_detail.serialize_json(
            value["front_of_queue"]
        )
    if "front_of_quota_shares" in value:
        import capo_batch.types.front_of_quota_shares_detail

        out["frontOfQuotaShares"] = (
            capo_batch.types.front_of_quota_shares_detail.serialize_json(
                value["front_of_quota_shares"]
            )
        )
    if "queue_utilization" in value:
        import capo_batch.types.queue_snapshot_utilization_detail

        out["queueUtilization"] = (
            capo_batch.types.queue_snapshot_utilization_detail.serialize_json(
                value["queue_utilization"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetJobQueueSnapshotResponse:
    out: GetJobQueueSnapshotResponse = {}  # type: ignore[typeddict-item]
    if "frontOfQueue" in data:
        import capo_batch.types.front_of_queue_detail

        out["front_of_queue"] = capo_batch.types.front_of_queue_detail.deserialize_json(
            data["frontOfQueue"]
        )
    if "frontOfQuotaShares" in data:
        import capo_batch.types.front_of_quota_shares_detail

        out["front_of_quota_shares"] = (
            capo_batch.types.front_of_quota_shares_detail.deserialize_json(
                data["frontOfQuotaShares"]
            )
        )
    if "queueUtilization" in data:
        import capo_batch.types.queue_snapshot_utilization_detail

        out["queue_utilization"] = (
            capo_batch.types.queue_snapshot_utilization_detail.deserialize_json(
                data["queueUtilization"]
            )
        )
    return out
