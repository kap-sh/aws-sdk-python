"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRateFilterName``."""

from typing import Literal, TypeAlias, cast

SavingsPlanRateFilterName: TypeAlias = Literal[
    "region",
    "instanceType",
    "productDescription",
    "tenancy",
    "productType",
    "serviceCode",
    "usageType",
    "operation",
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanRateFilterName) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanRateFilterName:
    return cast(SavingsPlanRateFilterName, data)
