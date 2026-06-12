"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_type

BillingGroupTypeList: TypeAlias = list[
    "aws_sdk_billingconductor.types.billing_group_type.BillingGroupType"
]


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupTypeList) -> list:
    import aws_sdk_billingconductor.types.billing_group_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_billingconductor.types.billing_group_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BillingGroupTypeList:
    import aws_sdk_billingconductor.types.billing_group_type

    out: BillingGroupTypeList = []
    for item in data:
        out.append(
            aws_sdk_billingconductor.types.billing_group_type.deserialize_json(item)
        )
    return out
