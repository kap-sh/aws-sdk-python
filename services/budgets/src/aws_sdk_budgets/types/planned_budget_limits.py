"""Generated from Smithy shape ``com.amazonaws.budgets#PlannedBudgetLimits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_budgets.types.generic_string
    import aws_sdk_budgets.types.spend

PlannedBudgetLimits: TypeAlias = dict[
    "aws_sdk_budgets.types.generic_string.GenericString",
    "aws_sdk_budgets.types.spend.Spend",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PlannedBudgetLimits) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_budgets.types.spend

        out[key] = aws_sdk_budgets.types.spend.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> PlannedBudgetLimits:
    out: PlannedBudgetLimits = {}
    for key, value in data.items():
        import aws_sdk_budgets.types.spend

        out[key] = aws_sdk_budgets.types.spend.deserialize_aws_json_1_1(value)
    return out
