"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_list_element

BillingGroupList: TypeAlias = list[
    "aws_sdk_billingconductor.types.billing_group_list_element.BillingGroupListElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupList) -> list:
    import aws_sdk_billingconductor.types.billing_group_list_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_billingconductor.types.billing_group_list_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BillingGroupList:
    import aws_sdk_billingconductor.types.billing_group_list_element

    out: BillingGroupList = []
    for item in data:
        out.append(
            aws_sdk_billingconductor.types.billing_group_list_element.deserialize_json(
                item
            )
        )
    return out
