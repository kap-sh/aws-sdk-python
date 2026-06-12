"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_status

BillingGroupStatusList: TypeAlias = list[
    "aws_sdk_billingconductor.types.billing_group_status.BillingGroupStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupStatusList) -> list:
    import aws_sdk_billingconductor.types.billing_group_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_billingconductor.types.billing_group_status.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BillingGroupStatusList:
    import aws_sdk_billingconductor.types.billing_group_status

    out: BillingGroupStatusList = []
    for item in data:
        out.append(
            aws_sdk_billingconductor.types.billing_group_status.deserialize_json(item)
        )
    return out
