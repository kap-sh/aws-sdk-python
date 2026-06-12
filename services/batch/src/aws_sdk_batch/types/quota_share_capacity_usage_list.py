"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareCapacityUsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.quota_share_capacity_usage

QuotaShareCapacityUsageList: TypeAlias = list[
    "aws_sdk_batch.types.quota_share_capacity_usage.QuotaShareCapacityUsage"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuotaShareCapacityUsageList) -> list:
    import aws_sdk_batch.types.quota_share_capacity_usage

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.quota_share_capacity_usage.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuotaShareCapacityUsageList:
    import aws_sdk_batch.types.quota_share_capacity_usage

    out: QuotaShareCapacityUsageList = []
    for item in data:
        out.append(
            aws_sdk_batch.types.quota_share_capacity_usage.deserialize_json(item)
        )
    return out
