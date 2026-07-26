"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillEstimateCommitmentSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.bill_estimate_commitment_summary

BillEstimateCommitmentSummaries: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.bill_estimate_commitment_summary.BillEstimateCommitmentSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillEstimateCommitmentSummaries) -> list:
    import capo_bcm_pricing_calculator.types.bill_estimate_commitment_summary

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.bill_estimate_commitment_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BillEstimateCommitmentSummaries:
    import capo_bcm_pricing_calculator.types.bill_estimate_commitment_summary

    out: BillEstimateCommitmentSummaries = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.bill_estimate_commitment_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
