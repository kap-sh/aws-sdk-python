"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_type

SavingsPlanTypeList: TypeAlias = list[
    "aws_sdk_savingsplans.types.savings_plan_type.SavingsPlanType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanTypeList) -> list:
    import aws_sdk_savingsplans.types.savings_plan_type

    out: list = []
    for item in value:
        out.append(aws_sdk_savingsplans.types.savings_plan_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SavingsPlanTypeList:
    import aws_sdk_savingsplans.types.savings_plan_type

    out: SavingsPlanTypeList = []
    for item in data:
        out.append(aws_sdk_savingsplans.types.savings_plan_type.deserialize_json(item))
    return out
