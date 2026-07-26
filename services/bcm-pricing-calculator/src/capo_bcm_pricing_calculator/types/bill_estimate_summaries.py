"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillEstimateSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.bill_estimate_summary

BillEstimateSummaries: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.bill_estimate_summary.BillEstimateSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillEstimateSummaries) -> list:
    import capo_bcm_pricing_calculator.types.bill_estimate_summary

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.bill_estimate_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BillEstimateSummaries:
    import capo_bcm_pricing_calculator.types.bill_estimate_summary

    out: BillEstimateSummaries = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.bill_estimate_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
