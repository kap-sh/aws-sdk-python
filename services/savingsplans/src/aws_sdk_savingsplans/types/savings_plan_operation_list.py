"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_operation

SavingsPlanOperationList: TypeAlias = list[
    "aws_sdk_savingsplans.types.savings_plan_operation.SavingsPlanOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOperationList) -> list:
    return list(value)


def deserialize_json(data: list) -> SavingsPlanOperationList:
    return list(data)
