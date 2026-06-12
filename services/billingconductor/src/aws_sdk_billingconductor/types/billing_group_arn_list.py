"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_arn

BillingGroupArnList: TypeAlias = list[
    "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> BillingGroupArnList:
    return list(data)
