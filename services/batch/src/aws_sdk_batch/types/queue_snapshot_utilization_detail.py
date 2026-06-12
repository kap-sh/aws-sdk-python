"""Generated from Smithy shape ``com.amazonaws.batch#QueueSnapshotUtilizationDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.fairshare_utilization_detail
    import aws_sdk_batch.types.long
    import aws_sdk_batch.types.queue_snapshot_capacity_usage_list
    import aws_sdk_batch.types.quota_share_utilization_detail


class QueueSnapshotUtilizationDetail(TypedDict):
    total_capacity_usage: NotRequired[
        "aws_sdk_batch.types.queue_snapshot_capacity_usage_list.QueueSnapshotCapacityUsageList"
    ]
    """<p>The total capacity usage for the entire job queue.</p>"""
    fairshare_utilization: NotRequired[
        "aws_sdk_batch.types.fairshare_utilization_detail.FairshareUtilizationDetail"
    ]
    """<p>The utilization information for a fairshare scheduling job queues, including active share count and top capacity utilization by share.</p>"""
    quota_share_utilization: NotRequired[
        "aws_sdk_batch.types.quota_share_utilization_detail.QuotaShareUtilizationDetail"
    ]
    """<p>The utilization information for a job queue with a quota share scheduling policy.</p>"""
    last_updated_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the queue utilization information was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueueSnapshotUtilizationDetail) -> dict:
    out: dict = {}
    if "total_capacity_usage" in value:
        import aws_sdk_batch.types.queue_snapshot_capacity_usage_list

        out["totalCapacityUsage"] = (
            aws_sdk_batch.types.queue_snapshot_capacity_usage_list.serialize_json(
                value["total_capacity_usage"]
            )
        )
    if "fairshare_utilization" in value:
        import aws_sdk_batch.types.fairshare_utilization_detail

        out["fairshareUtilization"] = (
            aws_sdk_batch.types.fairshare_utilization_detail.serialize_json(
                value["fairshare_utilization"]
            )
        )
    if "quota_share_utilization" in value:
        import aws_sdk_batch.types.quota_share_utilization_detail

        out["quotaShareUtilization"] = (
            aws_sdk_batch.types.quota_share_utilization_detail.serialize_json(
                value["quota_share_utilization"]
            )
        )
    if "last_updated_at" in value:
        out["lastUpdatedAt"] = value["last_updated_at"]
    return out


def deserialize_json(data: dict) -> QueueSnapshotUtilizationDetail:
    out: QueueSnapshotUtilizationDetail = {}  # type: ignore[typeddict-item]
    if "totalCapacityUsage" in data:
        import aws_sdk_batch.types.queue_snapshot_capacity_usage_list

        out["total_capacity_usage"] = (
            aws_sdk_batch.types.queue_snapshot_capacity_usage_list.deserialize_json(
                data["totalCapacityUsage"]
            )
        )
    if "fairshareUtilization" in data:
        import aws_sdk_batch.types.fairshare_utilization_detail

        out["fairshare_utilization"] = (
            aws_sdk_batch.types.fairshare_utilization_detail.deserialize_json(
                data["fairshareUtilization"]
            )
        )
    if "quotaShareUtilization" in data:
        import aws_sdk_batch.types.quota_share_utilization_detail

        out["quota_share_utilization"] = (
            aws_sdk_batch.types.quota_share_utilization_detail.deserialize_json(
                data["quotaShareUtilization"]
            )
        )
    if "lastUpdatedAt" in data:
        out["last_updated_at"] = data["lastUpdatedAt"]
    return out
