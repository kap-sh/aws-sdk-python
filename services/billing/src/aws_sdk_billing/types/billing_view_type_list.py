"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billing.types.billing_view_type

BillingViewTypeList: TypeAlias = list[
    "aws_sdk_billing.types.billing_view_type.BillingViewType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewTypeList) -> list:
    import aws_sdk_billing.types.billing_view_type

    out: list = []
    for item in value:
        out.append(aws_sdk_billing.types.billing_view_type.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> BillingViewTypeList:
    import aws_sdk_billing.types.billing_view_type

    out: BillingViewTypeList = []
    for item in data:
        out.append(
            aws_sdk_billing.types.billing_view_type.deserialize_aws_json_1_0(item)
        )
    return out
