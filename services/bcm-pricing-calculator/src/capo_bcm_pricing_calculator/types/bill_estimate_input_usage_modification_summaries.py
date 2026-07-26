"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillEstimateInputUsageModificationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.bill_estimate_input_usage_modification_summary

BillEstimateInputUsageModificationSummaries: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.bill_estimate_input_usage_modification_summary.BillEstimateInputUsageModificationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillEstimateInputUsageModificationSummaries) -> list:
    import capo_bcm_pricing_calculator.types.bill_estimate_input_usage_modification_summary

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.bill_estimate_input_usage_modification_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BillEstimateInputUsageModificationSummaries:
    import capo_bcm_pricing_calculator.types.bill_estimate_input_usage_modification_summary

    out: BillEstimateInputUsageModificationSummaries = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.bill_estimate_input_usage_modification_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
