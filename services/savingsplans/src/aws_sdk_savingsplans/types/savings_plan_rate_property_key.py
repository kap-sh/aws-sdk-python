"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRatePropertyKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_savingsplans.errors import DeserializationError

SavingsPlanRatePropertyKey: TypeAlias = Literal[
    "region",
    "instanceType",
    "instanceFamily",
    "productDescription",
    "tenancy",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "region",
        "instanceType",
        "instanceFamily",
        "productDescription",
        "tenancy",
    )
)


def serialize_json(value: SavingsPlanRatePropertyKey) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanRatePropertyKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SavingsPlanRatePropertyKey value: {data!r}"
        )
    return cast(SavingsPlanRatePropertyKey, data)
