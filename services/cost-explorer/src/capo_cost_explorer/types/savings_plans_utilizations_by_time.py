"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansUtilizationsByTime``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.savings_plans_utilization_by_time

SavingsPlansUtilizationsByTime: TypeAlias = list[
    "capo_cost_explorer.types.savings_plans_utilization_by_time.SavingsPlansUtilizationByTime"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansUtilizationsByTime) -> list:
    import capo_cost_explorer.types.savings_plans_utilization_by_time

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.savings_plans_utilization_by_time.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SavingsPlansUtilizationsByTime:
    import capo_cost_explorer.types.savings_plans_utilization_by_time

    out: SavingsPlansUtilizationsByTime = []
    for item in data:
        out.append(
            capo_cost_explorer.types.savings_plans_utilization_by_time.deserialize_aws_json_1_1(
                item
            )
        )
    return out
