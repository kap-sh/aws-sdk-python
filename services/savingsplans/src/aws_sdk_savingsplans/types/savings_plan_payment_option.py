"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanPaymentOption``."""

from typing import Literal, TypeAlias, cast

SavingsPlanPaymentOption: TypeAlias = Literal[
    "All Upfront",
    "Partial Upfront",
    "No Upfront",
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanPaymentOption) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanPaymentOption:
    return cast(SavingsPlanPaymentOption, data)
