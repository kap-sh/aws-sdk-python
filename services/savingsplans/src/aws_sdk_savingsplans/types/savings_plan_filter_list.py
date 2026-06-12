"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_filter

SavingsPlanFilterList: TypeAlias = list[
    "aws_sdk_savingsplans.types.savings_plan_filter.SavingsPlanFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanFilterList) -> list:
    import aws_sdk_savingsplans.types.savings_plan_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_savingsplans.types.savings_plan_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SavingsPlanFilterList:
    import aws_sdk_savingsplans.types.savings_plan_filter

    out: SavingsPlanFilterList = []
    for item in data:
        out.append(
            aws_sdk_savingsplans.types.savings_plan_filter.deserialize_json(item)
        )
    return out
