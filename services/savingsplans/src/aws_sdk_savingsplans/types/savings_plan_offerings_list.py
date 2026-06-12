"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_offering

SavingsPlanOfferingsList: TypeAlias = list[
    "aws_sdk_savingsplans.types.savings_plan_offering.SavingsPlanOffering"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOfferingsList) -> list:
    import aws_sdk_savingsplans.types.savings_plan_offering

    out: list = []
    for item in value:
        out.append(
            aws_sdk_savingsplans.types.savings_plan_offering.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SavingsPlanOfferingsList:
    import aws_sdk_savingsplans.types.savings_plan_offering

    out: SavingsPlanOfferingsList = []
    for item in data:
        out.append(
            aws_sdk_savingsplans.types.savings_plan_offering.deserialize_json(item)
        )
    return out
