"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareCapacityUtilizationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.quota_share_capacity_utilization

QuotaShareCapacityUtilizationList: TypeAlias = list[
    "capo_batch.types.quota_share_capacity_utilization.QuotaShareCapacityUtilization"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuotaShareCapacityUtilizationList) -> list:
    import capo_batch.types.quota_share_capacity_utilization

    out: list = []
    for item in value:
        out.append(
            capo_batch.types.quota_share_capacity_utilization.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> QuotaShareCapacityUtilizationList:
    import capo_batch.types.quota_share_capacity_utilization

    out: QuotaShareCapacityUtilizationList = []
    for item in data:
        out.append(
            capo_batch.types.quota_share_capacity_utilization.deserialize_json(item)
        )
    return out
