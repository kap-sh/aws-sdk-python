"""Generated from Smithy shape ``com.amazonaws.batch#SchedulingPolicyListingDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.scheduling_policy_listing_detail

SchedulingPolicyListingDetailList: TypeAlias = list[
    "aws_sdk_batch.types.scheduling_policy_listing_detail.SchedulingPolicyListingDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingPolicyListingDetailList) -> list:
    import aws_sdk_batch.types.scheduling_policy_listing_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_batch.types.scheduling_policy_listing_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SchedulingPolicyListingDetailList:
    import aws_sdk_batch.types.scheduling_policy_listing_detail

    out: SchedulingPolicyListingDetailList = []
    for item in data:
        out.append(
            aws_sdk_batch.types.scheduling_policy_listing_detail.deserialize_json(item)
        )
    return out
