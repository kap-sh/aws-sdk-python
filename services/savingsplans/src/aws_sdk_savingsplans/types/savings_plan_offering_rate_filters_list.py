"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingRateFiltersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_offering_rate_filter_element

SavingsPlanOfferingRateFiltersList: TypeAlias = list[
    "aws_sdk_savingsplans.types.savings_plan_offering_rate_filter_element.SavingsPlanOfferingRateFilterElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOfferingRateFiltersList) -> list:
    import aws_sdk_savingsplans.types.savings_plan_offering_rate_filter_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_savingsplans.types.savings_plan_offering_rate_filter_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SavingsPlanOfferingRateFiltersList:
    import aws_sdk_savingsplans.types.savings_plan_offering_rate_filter_element

    out: SavingsPlanOfferingRateFiltersList = []
    for item in data:
        out.append(
            aws_sdk_savingsplans.types.savings_plan_offering_rate_filter_element.deserialize_json(
                item
            )
        )
    return out
