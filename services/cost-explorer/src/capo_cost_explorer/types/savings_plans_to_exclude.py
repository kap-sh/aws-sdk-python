"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansToExclude``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.savings_plans_id

SavingsPlansToExclude: TypeAlias = list[
    "capo_cost_explorer.types.savings_plans_id.SavingsPlansId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansToExclude) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SavingsPlansToExclude:
    return list(data)
