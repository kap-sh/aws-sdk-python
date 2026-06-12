"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_savingsplans.errors import DeserializationError

SavingsPlanState: TypeAlias = Literal[
    "payment-pending",
    "payment-failed",
    "active",
    "retired",
    "queued",
    "queued-deleted",
    "pending-return",
    "returned",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "payment-pending",
        "payment-failed",
        "active",
        "retired",
        "queued",
        "queued-deleted",
        "pending-return",
        "returned",
    )
)


def serialize_json(value: SavingsPlanState) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SavingsPlanState value: {data!r}")
    return cast(SavingsPlanState, data)
