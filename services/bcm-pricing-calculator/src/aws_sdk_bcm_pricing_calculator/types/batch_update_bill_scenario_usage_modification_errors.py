"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateBillScenarioUsageModificationErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_error

BatchUpdateBillScenarioUsageModificationErrors: TypeAlias = list[
    "aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_error.BatchUpdateBillScenarioUsageModificationError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchUpdateBillScenarioUsageModificationErrors,
) -> list:
    import aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_error.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> BatchUpdateBillScenarioUsageModificationErrors:
    import aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_error

    out: BatchUpdateBillScenarioUsageModificationErrors = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out
