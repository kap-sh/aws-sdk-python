"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAndUsageComparisons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_and_usage_comparison

CostAndUsageComparisons: TypeAlias = list[
    "aws_sdk_cost_explorer.types.cost_and_usage_comparison.CostAndUsageComparison"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostAndUsageComparisons) -> list:
    import aws_sdk_cost_explorer.types.cost_and_usage_comparison

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.cost_and_usage_comparison.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CostAndUsageComparisons:
    import aws_sdk_cost_explorer.types.cost_and_usage_comparison

    out: CostAndUsageComparisons = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.cost_and_usage_comparison.deserialize_aws_json_1_1(
                item
            )
        )
    return out
