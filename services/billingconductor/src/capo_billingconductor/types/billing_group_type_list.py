"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_group_type

BillingGroupTypeList: TypeAlias = list[
    "capo_billingconductor.types.billing_group_type.BillingGroupType"
]


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupTypeList) -> list:
    import capo_billingconductor.types.billing_group_type

    out: list = []
    for item in value:
        out.append(capo_billingconductor.types.billing_group_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> BillingGroupTypeList:
    import capo_billingconductor.types.billing_group_type

    out: BillingGroupTypeList = []
    for item in data:
        out.append(
            capo_billingconductor.types.billing_group_type.deserialize_json(item)
        )
    return out
