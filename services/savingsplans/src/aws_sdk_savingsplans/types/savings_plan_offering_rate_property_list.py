"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingRatePropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_offering_rate_property

SavingsPlanOfferingRatePropertyList: TypeAlias = list[
    "aws_sdk_savingsplans.types.savings_plan_offering_rate_property.SavingsPlanOfferingRateProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOfferingRatePropertyList) -> list:
    import aws_sdk_savingsplans.types.savings_plan_offering_rate_property

    out: list = []
    for item in value:
        out.append(
            aws_sdk_savingsplans.types.savings_plan_offering_rate_property.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SavingsPlanOfferingRatePropertyList:
    import aws_sdk_savingsplans.types.savings_plan_offering_rate_property

    out: SavingsPlanOfferingRatePropertyList = []
    for item in data:
        out.append(
            aws_sdk_savingsplans.types.savings_plan_offering_rate_property.deserialize_json(
                item
            )
        )
    return out
