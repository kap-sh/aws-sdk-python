"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillEstimateInputCommitmentModificationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.bill_estimate_input_commitment_modification_summary

BillEstimateInputCommitmentModificationSummaries: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.bill_estimate_input_commitment_modification_summary.BillEstimateInputCommitmentModificationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BillEstimateInputCommitmentModificationSummaries,
) -> list:
    import capo_bcm_pricing_calculator.types.bill_estimate_input_commitment_modification_summary

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.bill_estimate_input_commitment_modification_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> BillEstimateInputCommitmentModificationSummaries:
    import capo_bcm_pricing_calculator.types.bill_estimate_input_commitment_modification_summary

    out: BillEstimateInputCommitmentModificationSummaries = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.bill_estimate_input_commitment_modification_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
