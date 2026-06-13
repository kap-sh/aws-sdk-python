"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billing.types.billing_view_list_element

BillingViewList: TypeAlias = list[
    "aws_sdk_billing.types.billing_view_list_element.BillingViewListElement"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewList) -> list:
    import aws_sdk_billing.types.billing_view_list_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_billing.types.billing_view_list_element.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BillingViewList:
    import aws_sdk_billing.types.billing_view_list_element

    out: BillingViewList = []
    for item in data:
        out.append(
            aws_sdk_billing.types.billing_view_list_element.deserialize_aws_json_1_0(
                item
            )
        )
    return out
