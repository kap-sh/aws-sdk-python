"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlansFilterName``."""

from typing import Literal, TypeAlias, cast

SavingsPlansFilterName: TypeAlias = Literal[
    "region",
    "ec2-instance-family",
    "commitment",
    "upfront",
    "term",
    "savings-plan-type",
    "payment-option",
    "start",
    "end",
    "instance-family",
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlansFilterName) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlansFilterName:
    return cast(SavingsPlansFilterName, data)
