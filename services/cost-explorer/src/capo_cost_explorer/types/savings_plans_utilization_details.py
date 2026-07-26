"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansUtilizationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.savings_plans_utilization_detail

SavingsPlansUtilizationDetails: TypeAlias = list[
    "capo_cost_explorer.types.savings_plans_utilization_detail.SavingsPlansUtilizationDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansUtilizationDetails) -> list:
    import capo_cost_explorer.types.savings_plans_utilization_detail

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.savings_plans_utilization_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SavingsPlansUtilizationDetails:
    import capo_cost_explorer.types.savings_plans_utilization_detail

    out: SavingsPlansUtilizationDetails = []
    for item in data:
        out.append(
            capo_cost_explorer.types.savings_plans_utilization_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
