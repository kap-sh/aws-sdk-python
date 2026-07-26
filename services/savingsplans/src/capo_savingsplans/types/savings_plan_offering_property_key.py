"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingPropertyKey``."""

from typing import Literal, TypeAlias, cast

SavingsPlanOfferingPropertyKey: TypeAlias = Literal[
    "region",
    "instanceFamily",
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOfferingPropertyKey) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanOfferingPropertyKey:
    return cast(SavingsPlanOfferingPropertyKey, data)
