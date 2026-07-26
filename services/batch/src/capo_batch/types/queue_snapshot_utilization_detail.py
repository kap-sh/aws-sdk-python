"""Generated from Smithy shape ``com.amazonaws.batch#QueueSnapshotUtilizationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.fairshare_utilization_detail
    import capo_batch.types.long
    import capo_batch.types.queue_snapshot_capacity_usage_list
    import capo_batch.types.quota_share_utilization_detail


class QueueSnapshotUtilizationDetail(TypedDict, closed=True):
    total_capacity_usage: NotRequired[
        "capo_batch.types.queue_snapshot_capacity_usage_list.QueueSnapshotCapacityUsageList"
    ]
    """<p>The total capacity usage for the entire job queue.</p>"""
    fairshare_utilization: NotRequired[
        "capo_batch.types.fairshare_utilization_detail.FairshareUtilizationDetail"
    ]
    """<p>The utilization information for a fairshare scheduling job queues, including active share count and top capacity utilization by share.</p>"""
    quota_share_utilization: NotRequired[
        "capo_batch.types.quota_share_utilization_detail.QuotaShareUtilizationDetail"
    ]
    """<p>The utilization information for a job queue with a quota share scheduling policy.</p>"""
    last_updated_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the queue utilization information was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueueSnapshotUtilizationDetail) -> dict:
    out: dict = {}
    if "total_capacity_usage" in value:
        import capo_batch.types.queue_snapshot_capacity_usage_list

        out["totalCapacityUsage"] = (
            capo_batch.types.queue_snapshot_capacity_usage_list.serialize_json(
                value["total_capacity_usage"]
            )
        )
    if "fairshare_utilization" in value:
        import capo_batch.types.fairshare_utilization_detail

        out["fairshareUtilization"] = (
            capo_batch.types.fairshare_utilization_detail.serialize_json(
                value["fairshare_utilization"]
            )
        )
    if "quota_share_utilization" in value:
        import capo_batch.types.quota_share_utilization_detail

        out["quotaShareUtilization"] = (
            capo_batch.types.quota_share_utilization_detail.serialize_json(
                value["quota_share_utilization"]
            )
        )
    if "last_updated_at" in value:
        out["lastUpdatedAt"] = value["last_updated_at"]
    return out


def deserialize_json(data: dict) -> QueueSnapshotUtilizationDetail:
    out: QueueSnapshotUtilizationDetail = {}  # type: ignore[typeddict-item]
    if "totalCapacityUsage" in data:
        import capo_batch.types.queue_snapshot_capacity_usage_list

        out["total_capacity_usage"] = (
            capo_batch.types.queue_snapshot_capacity_usage_list.deserialize_json(
                data["totalCapacityUsage"]
            )
        )
    if "fairshareUtilization" in data:
        import capo_batch.types.fairshare_utilization_detail

        out["fairshare_utilization"] = (
            capo_batch.types.fairshare_utilization_detail.deserialize_json(
                data["fairshareUtilization"]
            )
        )
    if "quotaShareUtilization" in data:
        import capo_batch.types.quota_share_utilization_detail

        out["quota_share_utilization"] = (
            capo_batch.types.quota_share_utilization_detail.deserialize_json(
                data["quotaShareUtilization"]
            )
        )
    if "lastUpdatedAt" in data:
        out["last_updated_at"] = data["lastUpdatedAt"]
    return out
