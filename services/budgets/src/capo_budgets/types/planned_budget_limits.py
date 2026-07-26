"""Generated from Smithy shape ``com.amazonaws.budgets#PlannedBudgetLimits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.generic_string
    import capo_budgets.types.spend

PlannedBudgetLimits: TypeAlias = dict[
    "capo_budgets.types.generic_string.GenericString", "capo_budgets.types.spend.Spend"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PlannedBudgetLimits) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_budgets.types.spend

        out[key] = capo_budgets.types.spend.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> PlannedBudgetLimits:
    out: PlannedBudgetLimits = {}
    for key, value in data.items():
        import capo_budgets.types.spend

        out[key] = capo_budgets.types.spend.deserialize_aws_json_1_1(value)
    return out
