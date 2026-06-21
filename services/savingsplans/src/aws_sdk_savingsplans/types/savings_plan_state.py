"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanState``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: SavingsPlanState) -> str:
    return value


def deserialize_json(data: str) -> SavingsPlanState:
    return cast(SavingsPlanState, data)
