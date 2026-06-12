"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansToAdd``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.savings_plans

SavingsPlansToAdd: TypeAlias = list[
    "aws_sdk_cost_explorer.types.savings_plans.SavingsPlans"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansToAdd) -> list:
    import aws_sdk_cost_explorer.types.savings_plans

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.savings_plans.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SavingsPlansToAdd:
    import aws_sdk_cost_explorer.types.savings_plans

    out: SavingsPlansToAdd = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.savings_plans.deserialize_aws_json_1_1(item)
        )
    return out
