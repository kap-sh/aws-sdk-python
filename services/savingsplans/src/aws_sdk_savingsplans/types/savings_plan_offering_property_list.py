"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingPropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_offering_property

SavingsPlanOfferingPropertyList: TypeAlias = list[
    "aws_sdk_savingsplans.types.savings_plan_offering_property.SavingsPlanOfferingProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOfferingPropertyList) -> list:
    import aws_sdk_savingsplans.types.savings_plan_offering_property

    out: list = []
    for item in value:
        out.append(
            aws_sdk_savingsplans.types.savings_plan_offering_property.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SavingsPlanOfferingPropertyList:
    import aws_sdk_savingsplans.types.savings_plan_offering_property

    out: SavingsPlanOfferingPropertyList = []
    for item in data:
        out.append(
            aws_sdk_savingsplans.types.savings_plan_offering_property.deserialize_json(
                item
            )
        )
    return out
