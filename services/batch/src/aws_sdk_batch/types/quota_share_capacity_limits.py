"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareCapacityLimits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.quota_share_capacity_limit

QuotaShareCapacityLimits: TypeAlias = list[
    "aws_sdk_batch.types.quota_share_capacity_limit.QuotaShareCapacityLimit"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuotaShareCapacityLimits) -> list:
    import aws_sdk_batch.types.quota_share_capacity_limit

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.quota_share_capacity_limit.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuotaShareCapacityLimits:
    import aws_sdk_batch.types.quota_share_capacity_limit

    out: QuotaShareCapacityLimits = []
    for item in data:
        out.append(
            aws_sdk_batch.types.quota_share_capacity_limit.deserialize_json(item)
        )
    return out
