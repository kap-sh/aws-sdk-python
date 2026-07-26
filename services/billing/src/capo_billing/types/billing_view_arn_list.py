"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.billing_view_arn

BillingViewArnList: TypeAlias = list[
    "capo_billing.types.billing_view_arn.BillingViewArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewArnList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> BillingViewArnList:
    return list(data)
