"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioUsageModificationErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_error

BatchCreateBillScenarioUsageModificationErrors: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_error.BatchCreateBillScenarioUsageModificationError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchCreateBillScenarioUsageModificationErrors,
) -> list:
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_error

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_error.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> BatchCreateBillScenarioUsageModificationErrors:
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_error

    out: BatchCreateBillScenarioUsageModificationErrors = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out
