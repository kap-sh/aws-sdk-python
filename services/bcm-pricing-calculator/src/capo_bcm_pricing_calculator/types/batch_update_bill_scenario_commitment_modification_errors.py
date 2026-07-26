"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateBillScenarioCommitmentModificationErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_error

BatchUpdateBillScenarioCommitmentModificationErrors: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_error.BatchUpdateBillScenarioCommitmentModificationError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchUpdateBillScenarioCommitmentModificationErrors,
) -> list:
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_error

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_error.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> BatchUpdateBillScenarioCommitmentModificationErrors:
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_error

    out: BatchUpdateBillScenarioCommitmentModificationErrors = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out
