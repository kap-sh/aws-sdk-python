"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRateFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_savingsplans.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "region",
        "instanceType",
        "productDescription",
        "tenancy",
        "productType",
        "serviceCode",
        "usageType",
        "operation",
    )
)


def serialize_json(value: SavingsPlanRateFilterName) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanRateFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SavingsPlanRateFilterName value: {data!r}")
    return cast(SavingsPlanRateFilterName, data)
