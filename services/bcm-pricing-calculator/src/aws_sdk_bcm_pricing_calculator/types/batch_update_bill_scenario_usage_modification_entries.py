"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateBillScenarioUsageModificationEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entry

BatchUpdateBillScenarioUsageModificationEntries: TypeAlias = list[
    "aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entry.BatchUpdateBillScenarioUsageModificationEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchUpdateBillScenarioUsageModificationEntries,
) -> list:
    import aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> BatchUpdateBillScenarioUsageModificationEntries:
    import aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entry

    out: BatchUpdateBillScenarioUsageModificationEntries = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
