"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateBillScenarioCommitmentModificationEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_entry

BatchUpdateBillScenarioCommitmentModificationEntries: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_entry.BatchUpdateBillScenarioCommitmentModificationEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchUpdateBillScenarioCommitmentModificationEntries,
) -> list:
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_entry

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> BatchUpdateBillScenarioCommitmentModificationEntries:
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_entry

    out: BatchUpdateBillScenarioCommitmentModificationEntries = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
