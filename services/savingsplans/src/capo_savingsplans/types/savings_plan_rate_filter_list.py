"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRateFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_rate_filter

SavingsPlanRateFilterList: TypeAlias = list[
    "capo_savingsplans.types.savings_plan_rate_filter.SavingsPlanRateFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanRateFilterList) -> list:
    import capo_savingsplans.types.savings_plan_rate_filter

    out: list = []
    for item in value:
        out.append(
            capo_savingsplans.types.savings_plan_rate_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SavingsPlanRateFilterList:
    import capo_savingsplans.types.savings_plan_rate_filter

    out: SavingsPlanRateFilterList = []
    for item in data:
        out.append(
            capo_savingsplans.types.savings_plan_rate_filter.deserialize_json(item)
        )
    return out
