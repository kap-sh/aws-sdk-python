"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillEstimateLineItemSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.bill_estimate_line_item_summary

BillEstimateLineItemSummaries: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.bill_estimate_line_item_summary.BillEstimateLineItemSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillEstimateLineItemSummaries) -> list:
    import capo_bcm_pricing_calculator.types.bill_estimate_line_item_summary

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.bill_estimate_line_item_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BillEstimateLineItemSummaries:
    import capo_bcm_pricing_calculator.types.bill_estimate_line_item_summary

    out: BillEstimateLineItemSummaries = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.bill_estimate_line_item_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
