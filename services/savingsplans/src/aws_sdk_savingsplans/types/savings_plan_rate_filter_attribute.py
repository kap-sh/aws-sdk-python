"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRateFilterAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_savingsplans.errors import DeserializationError

SavingsPlanRateFilterAttribute: TypeAlias = Literal[
    "region",
    "instanceFamily",
    "instanceType",
    "productDescription",
    "tenancy",
    "productId",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "region",
        "instanceFamily",
        "instanceType",
        "productDescription",
        "tenancy",
        "productId",
    )
)


def serialize_json(value: SavingsPlanRateFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanRateFilterAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SavingsPlanRateFilterAttribute value: {data!r}"
        )
    return cast(SavingsPlanRateFilterAttribute, data)
