"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingFiltersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_offering_filter_element

SavingsPlanOfferingFiltersList: TypeAlias = list[
    "capo_savingsplans.types.savings_plan_offering_filter_element.SavingsPlanOfferingFilterElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOfferingFiltersList) -> list:
    import capo_savingsplans.types.savings_plan_offering_filter_element

    out: list = []
    for item in value:
        out.append(
            capo_savingsplans.types.savings_plan_offering_filter_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SavingsPlanOfferingFiltersList:
    import capo_savingsplans.types.savings_plan_offering_filter_element

    out: SavingsPlanOfferingFiltersList = []
    for item in data:
        out.append(
            capo_savingsplans.types.savings_plan_offering_filter_element.deserialize_json(
                item
            )
        )
    return out
