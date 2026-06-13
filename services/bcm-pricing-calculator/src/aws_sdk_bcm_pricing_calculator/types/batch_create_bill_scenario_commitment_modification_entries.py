"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioCommitmentModificationEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entry

BatchCreateBillScenarioCommitmentModificationEntries: TypeAlias = list[
    "aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entry.BatchCreateBillScenarioCommitmentModificationEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchCreateBillScenarioCommitmentModificationEntries,
) -> list:
    import aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> BatchCreateBillScenarioCommitmentModificationEntries:
    import aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entry

    out: BatchCreateBillScenarioCommitmentModificationEntries = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
