"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_group_status

BillingGroupStatusList: TypeAlias = list[
    "capo_billingconductor.types.billing_group_status.BillingGroupStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupStatusList) -> list:
    import capo_billingconductor.types.billing_group_status

    out: list = []
    for item in value:
        out.append(
            capo_billingconductor.types.billing_group_status.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BillingGroupStatusList:
    import capo_billingconductor.types.billing_group_status

    out: BillingGroupStatusList = []
    for item in data:
        out.append(
            capo_billingconductor.types.billing_group_status.deserialize_json(item)
        )
    return out
