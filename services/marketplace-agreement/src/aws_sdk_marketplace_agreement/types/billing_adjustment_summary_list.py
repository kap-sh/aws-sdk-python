"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BillingAdjustmentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.billing_adjustment_summary

BillingAdjustmentSummaryList: TypeAlias = list[
    "aws_sdk_marketplace_agreement.types.billing_adjustment_summary.BillingAdjustmentSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingAdjustmentSummaryList) -> list:
    import aws_sdk_marketplace_agreement.types.billing_adjustment_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_agreement.types.billing_adjustment_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BillingAdjustmentSummaryList:
    import aws_sdk_marketplace_agreement.types.billing_adjustment_summary

    out: BillingAdjustmentSummaryList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_agreement.types.billing_adjustment_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
