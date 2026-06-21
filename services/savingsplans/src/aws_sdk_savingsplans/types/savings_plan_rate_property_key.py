"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRatePropertyKey``."""

from typing import Literal, TypeAlias, cast

SavingsPlanRatePropertyKey: TypeAlias = Literal[
    "region",
    "instanceType",
    "instanceFamily",
    "productDescription",
    "tenancy",
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanRatePropertyKey) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanRatePropertyKey:
    return cast(SavingsPlanRatePropertyKey, data)
