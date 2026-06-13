"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillScenarioUsageModificationItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.bill_scenario_usage_modification_item

BillScenarioUsageModificationItems: TypeAlias = list[
    "aws_sdk_bcm_pricing_calculator.types.bill_scenario_usage_modification_item.BillScenarioUsageModificationItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillScenarioUsageModificationItems) -> list:
    import aws_sdk_bcm_pricing_calculator.types.bill_scenario_usage_modification_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.bill_scenario_usage_modification_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BillScenarioUsageModificationItems:
    import aws_sdk_bcm_pricing_calculator.types.bill_scenario_usage_modification_item

    out: BillScenarioUsageModificationItems = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.bill_scenario_usage_modification_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
