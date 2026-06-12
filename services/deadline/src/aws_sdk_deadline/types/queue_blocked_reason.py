"""Generated from Smithy shape ``com.amazonaws.deadline#QueueBlockedReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

QueueBlockedReason: TypeAlias = Literal[
    "NO_BUDGET_CONFIGURED",
    "BUDGET_THRESHOLD_REACHED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_BUDGET_CONFIGURED",
        "BUDGET_THRESHOLD_REACHED",
    )
)


def serialize_json(value: QueueBlockedReason) -> str:
    return value


def deserialize_json(data: str) -> QueueBlockedReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueueBlockedReason value: {data!r}")
    return cast(QueueBlockedReason, data)
