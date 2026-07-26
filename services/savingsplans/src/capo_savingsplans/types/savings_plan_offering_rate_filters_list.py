"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingRateFiltersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_offering_rate_filter_element

SavingsPlanOfferingRateFiltersList: TypeAlias = list[
    "capo_savingsplans.types.savings_plan_offering_rate_filter_element.SavingsPlanOfferingRateFilterElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOfferingRateFiltersList) -> list:
    import capo_savingsplans.types.savings_plan_offering_rate_filter_element

    out: list = []
    for item in value:
        out.append(
            capo_savingsplans.types.savings_plan_offering_rate_filter_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SavingsPlanOfferingRateFiltersList:
    import capo_savingsplans.types.savings_plan_offering_rate_filter_element

    out: SavingsPlanOfferingRateFiltersList = []
    for item in data:
        out.append(
            capo_savingsplans.types.savings_plan_offering_rate_filter_element.deserialize_json(
                item
            )
        )
    return out
