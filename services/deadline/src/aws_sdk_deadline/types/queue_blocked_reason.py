"""Generated from Smithy shape ``com.amazonaws.deadline#QueueBlockedReason``."""

from typing import Literal, TypeAlias, cast

QueueBlockedReason: TypeAlias = Literal[
    "NO_BUDGET_CONFIGURED",
    "BUDGET_THRESHOLD_REACHED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueueBlockedReason) -> str:
    return value


def deserialize_json(data: str) -> QueueBlockedReason:
    return cast(QueueBlockedReason, data)
