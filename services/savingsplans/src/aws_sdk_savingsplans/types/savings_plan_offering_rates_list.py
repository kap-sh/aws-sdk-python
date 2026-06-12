"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingRatesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_offering_rate

SavingsPlanOfferingRatesList: TypeAlias = list[
    "aws_sdk_savingsplans.types.savings_plan_offering_rate.SavingsPlanOfferingRate"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOfferingRatesList) -> list:
    import aws_sdk_savingsplans.types.savings_plan_offering_rate

    out: list = []
    for item in value:
        out.append(
            aws_sdk_savingsplans.types.savings_plan_offering_rate.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SavingsPlanOfferingRatesList:
    import aws_sdk_savingsplans.types.savings_plan_offering_rate

    out: SavingsPlanOfferingRatesList = []
    for item in data:
        out.append(
            aws_sdk_savingsplans.types.savings_plan_offering_rate.deserialize_json(item)
        )
    return out
