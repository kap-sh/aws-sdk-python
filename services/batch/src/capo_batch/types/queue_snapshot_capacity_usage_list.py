"""Generated from Smithy shape ``com.amazonaws.batch#QueueSnapshotCapacityUsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.queue_snapshot_capacity_usage

QueueSnapshotCapacityUsageList: TypeAlias = list[
    "capo_batch.types.queue_snapshot_capacity_usage.QueueSnapshotCapacityUsage"
]


# --- restJson1 ser/de ---
def serialize_json(value: QueueSnapshotCapacityUsageList) -> list:
    import capo_batch.types.queue_snapshot_capacity_usage

    out: list = []
    for item in value:
        out.append(capo_batch.types.queue_snapshot_capacity_usage.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueueSnapshotCapacityUsageList:
    import capo_batch.types.queue_snapshot_capacity_usage

    out: QueueSnapshotCapacityUsageList = []
    for item in data:
        out.append(
            capo_batch.types.queue_snapshot_capacity_usage.deserialize_json(item)
        )
    return out
