"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanPaymentOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_savingsplans.errors import DeserializationError

SavingsPlanPaymentOption: TypeAlias = Literal[
    "All Upfront",
    "Partial Upfront",
    "No Upfront",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "All Upfront",
        "Partial Upfront",
        "No Upfront",
    )
)


def serialize_json(value: SavingsPlanPaymentOption) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanPaymentOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SavingsPlanPaymentOption value: {data!r}")
    return cast(SavingsPlanPaymentOption, data)
