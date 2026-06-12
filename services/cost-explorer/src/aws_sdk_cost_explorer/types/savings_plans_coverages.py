"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansCoverages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.savings_plans_coverage

SavingsPlansCoverages: TypeAlias = list[
    "aws_sdk_cost_explorer.types.savings_plans_coverage.SavingsPlansCoverage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansCoverages) -> list:
    import aws_sdk_cost_explorer.types.savings_plans_coverage

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.savings_plans_coverage.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SavingsPlansCoverages:
    import aws_sdk_cost_explorer.types.savings_plans_coverage

    out: SavingsPlansCoverages = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.savings_plans_coverage.deserialize_aws_json_1_1(
                item
            )
        )
    return out
