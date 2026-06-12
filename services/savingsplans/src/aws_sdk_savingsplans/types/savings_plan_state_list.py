"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_state

SavingsPlanStateList: TypeAlias = list[
    "aws_sdk_savingsplans.types.savings_plan_state.SavingsPlanState"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanStateList) -> list:
    import aws_sdk_savingsplans.types.savings_plan_state

    out: list = []
    for item in value:
        out.append(aws_sdk_savingsplans.types.savings_plan_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> SavingsPlanStateList:
    import aws_sdk_savingsplans.types.savings_plan_state

    out: SavingsPlanStateList = []
    for item in data:
        out.append(aws_sdk_savingsplans.types.savings_plan_state.deserialize_json(item))
    return out
