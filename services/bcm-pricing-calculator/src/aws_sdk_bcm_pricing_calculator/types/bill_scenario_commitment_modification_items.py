"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillScenarioCommitmentModificationItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_item

BillScenarioCommitmentModificationItems: TypeAlias = list[
    "aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_item.BillScenarioCommitmentModificationItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillScenarioCommitmentModificationItems) -> list:
    import aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BillScenarioCommitmentModificationItems:
    import aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_item

    out: BillScenarioCommitmentModificationItems = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
