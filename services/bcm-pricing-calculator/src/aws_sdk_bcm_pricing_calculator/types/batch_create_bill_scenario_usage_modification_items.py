"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioUsageModificationItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_item

BatchCreateBillScenarioUsageModificationItems: TypeAlias = list[
    "aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_item.BatchCreateBillScenarioUsageModificationItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchCreateBillScenarioUsageModificationItems,
) -> list:
    import aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> BatchCreateBillScenarioUsageModificationItems:
    import aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_item

    out: BatchCreateBillScenarioUsageModificationItems = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
