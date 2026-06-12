"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_savingsplans.errors import DeserializationError

SavingsPlanType: TypeAlias = Literal[
    "Compute",
    "EC2Instance",
    "SageMaker",
    "Database",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Compute",
        "EC2Instance",
        "SageMaker",
        "Database",
    )
)


def serialize_json(value: SavingsPlanType) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SavingsPlanType value: {data!r}")
    return cast(SavingsPlanType, data)
