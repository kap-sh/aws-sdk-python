"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRateServiceCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_rate_service_code

SavingsPlanRateServiceCodeList: TypeAlias = list[
    "aws_sdk_savingsplans.types.savings_plan_rate_service_code.SavingsPlanRateServiceCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanRateServiceCodeList) -> list:
    import aws_sdk_savingsplans.types.savings_plan_rate_service_code

    out: list = []
    for item in value:
        out.append(
            aws_sdk_savingsplans.types.savings_plan_rate_service_code.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SavingsPlanRateServiceCodeList:
    import aws_sdk_savingsplans.types.savings_plan_rate_service_code

    out: SavingsPlanRateServiceCodeList = []
    for item in data:
        out.append(
            aws_sdk_savingsplans.types.savings_plan_rate_service_code.deserialize_json(
                item
            )
        )
    return out
