"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan

SavingsPlanList: TypeAlias = list["aws_sdk_savingsplans.types.savings_plan.SavingsPlan"]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanList) -> list:
    import aws_sdk_savingsplans.types.savings_plan

    out: list = []
    for item in value:
        out.append(aws_sdk_savingsplans.types.savings_plan.serialize_json(item))
    return out


def deserialize_json(data: list) -> SavingsPlanList:
    import aws_sdk_savingsplans.types.savings_plan

    out: SavingsPlanList = []
    for item in data:
        out.append(aws_sdk_savingsplans.types.savings_plan.deserialize_json(item))
    return out
