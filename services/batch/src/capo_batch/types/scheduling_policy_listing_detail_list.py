"""Generated from Smithy shape ``com.amazonaws.batch#SchedulingPolicyListingDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.scheduling_policy_listing_detail

SchedulingPolicyListingDetailList: TypeAlias = list[
    "capo_batch.types.scheduling_policy_listing_detail.SchedulingPolicyListingDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingPolicyListingDetailList) -> list:
    import capo_batch.types.scheduling_policy_listing_detail

    out: list = []
    for item in value:
        out.append(
            capo_batch.types.scheduling_policy_listing_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SchedulingPolicyListingDetailList:
    import capo_batch.types.scheduling_policy_listing_detail

    out: SchedulingPolicyListingDetailList = []
    for item in data:
        out.append(
            capo_batch.types.scheduling_policy_listing_detail.deserialize_json(item)
        )
    return out
