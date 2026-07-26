"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansCoverages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.savings_plans_coverage

SavingsPlansCoverages: TypeAlias = list[
    "capo_cost_explorer.types.savings_plans_coverage.SavingsPlansCoverage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansCoverages) -> list:
    import capo_cost_explorer.types.savings_plans_coverage

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.savings_plans_coverage.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SavingsPlansCoverages:
    import capo_cost_explorer.types.savings_plans_coverage

    out: SavingsPlansCoverages = []
    for item in data:
        out.append(
            capo_cost_explorer.types.savings_plans_coverage.deserialize_aws_json_1_1(
                item
            )
        )
    return out
