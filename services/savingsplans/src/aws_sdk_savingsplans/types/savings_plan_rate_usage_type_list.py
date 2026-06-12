"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRateUsageTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_rate_usage_type

SavingsPlanRateUsageTypeList: TypeAlias = list[
    "aws_sdk_savingsplans.types.savings_plan_rate_usage_type.SavingsPlanRateUsageType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanRateUsageTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> SavingsPlanRateUsageTypeList:
    return list(data)
