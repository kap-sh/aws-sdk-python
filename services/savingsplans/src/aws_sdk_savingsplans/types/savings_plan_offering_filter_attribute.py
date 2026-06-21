"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingFilterAttribute``."""

from typing import Literal, TypeAlias, cast

SavingsPlanOfferingFilterAttribute: TypeAlias = Literal[
    "region",
    "instanceFamily",
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOfferingFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanOfferingFilterAttribute:
    return cast(SavingsPlanOfferingFilterAttribute, data)
