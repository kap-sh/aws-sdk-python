"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRateServiceCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_rate_service_code

SavingsPlanRateServiceCodeList: TypeAlias = list[
    "capo_savingsplans.types.savings_plan_rate_service_code.SavingsPlanRateServiceCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanRateServiceCodeList) -> list:
    import capo_savingsplans.types.savings_plan_rate_service_code

    out: list = []
    for item in value:
        out.append(
            capo_savingsplans.types.savings_plan_rate_service_code.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SavingsPlanRateServiceCodeList:
    import capo_savingsplans.types.savings_plan_rate_service_code

    out: SavingsPlanRateServiceCodeList = []
    for item in data:
        out.append(
            capo_savingsplans.types.savings_plan_rate_service_code.deserialize_json(
                item
            )
        )
    return out
