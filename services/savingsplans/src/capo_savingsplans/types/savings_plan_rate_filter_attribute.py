"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRateFilterAttribute``."""

from typing import Literal, TypeAlias, cast

SavingsPlanRateFilterAttribute: TypeAlias = Literal[
    "region",
    "instanceFamily",
    "instanceType",
    "productDescription",
    "tenancy",
    "productId",
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanRateFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanRateFilterAttribute:
    return cast(SavingsPlanRateFilterAttribute, data)
