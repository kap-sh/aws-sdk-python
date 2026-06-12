"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostComparisonDrivers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_comparison_driver

CostComparisonDrivers: TypeAlias = list[
    "aws_sdk_cost_explorer.types.cost_comparison_driver.CostComparisonDriver"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostComparisonDrivers) -> list:
    import aws_sdk_cost_explorer.types.cost_comparison_driver

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.cost_comparison_driver.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CostComparisonDrivers:
    import aws_sdk_cost_explorer.types.cost_comparison_driver

    out: CostComparisonDrivers = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.cost_comparison_driver.deserialize_aws_json_1_1(
                item
            )
        )
    return out
