"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingPropertyKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_savingsplans.errors import DeserializationError

SavingsPlanOfferingPropertyKey: TypeAlias = Literal[
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


def serialize_json(value: SavingsPlanOfferingPropertyKey) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanOfferingPropertyKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SavingsPlanOfferingPropertyKey value: {data!r}"
        )
    return cast(SavingsPlanOfferingPropertyKey, data)
