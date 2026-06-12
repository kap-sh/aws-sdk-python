"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingFilterAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_savingsplans.errors import DeserializationError

SavingsPlanOfferingFilterAttribute: TypeAlias = Literal[
    "region",
    "instanceFamily",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "region",
        "instanceFamily",
    )
)


def serialize_json(value: SavingsPlanOfferingFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanOfferingFilterAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SavingsPlanOfferingFilterAttribute value: {data!r}"
        )
    return cast(SavingsPlanOfferingFilterAttribute, data)
