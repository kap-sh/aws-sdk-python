"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanPaymentOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_payment_option

SavingsPlanPaymentOptionList: TypeAlias = list[
    "capo_savingsplans.types.savings_plan_payment_option.SavingsPlanPaymentOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanPaymentOptionList) -> list:
    import capo_savingsplans.types.savings_plan_payment_option

    out: list = []
    for item in value:
        out.append(
            capo_savingsplans.types.savings_plan_payment_option.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SavingsPlanPaymentOptionList:
    import capo_savingsplans.types.savings_plan_payment_option

    out: SavingsPlanPaymentOptionList = []
    for item in data:
        out.append(
            capo_savingsplans.types.savings_plan_payment_option.deserialize_json(item)
        )
    return out
