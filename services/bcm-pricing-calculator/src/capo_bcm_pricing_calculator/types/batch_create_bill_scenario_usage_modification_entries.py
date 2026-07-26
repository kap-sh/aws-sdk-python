"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioUsageModificationEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_entry

BatchCreateBillScenarioUsageModificationEntries: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_entry.BatchCreateBillScenarioUsageModificationEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchCreateBillScenarioUsageModificationEntries,
) -> list:
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_entry

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> BatchCreateBillScenarioUsageModificationEntries:
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_entry

    out: BatchCreateBillScenarioUsageModificationEntries = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
