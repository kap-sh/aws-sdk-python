"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioCommitmentModificationItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_item

BatchCreateBillScenarioCommitmentModificationItems: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_item.BatchCreateBillScenarioCommitmentModificationItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchCreateBillScenarioCommitmentModificationItems,
) -> list:
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_item

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> BatchCreateBillScenarioCommitmentModificationItems:
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_item

    out: BatchCreateBillScenarioCommitmentModificationItems = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
