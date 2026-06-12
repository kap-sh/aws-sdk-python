"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlansFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_savingsplans.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: SavingsPlansFilterName) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlansFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SavingsPlansFilterName value: {data!r}")
    return cast(SavingsPlansFilterName, data)
