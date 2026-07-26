"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanType``."""

from typing import Literal, TypeAlias, cast

SavingsPlanType: TypeAlias = Literal[
    "Compute",
    "EC2Instance",
    "SageMaker",
    "Database",
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanType) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanType:
    return cast(SavingsPlanType, data)
