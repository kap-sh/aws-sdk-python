"""Generated from Smithy shape ``com.amazonaws.deadline#QueueLimitAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

QueueLimitAssociationStatus: TypeAlias = Literal[
    "ACTIVE",
    "STOP_LIMIT_USAGE_AND_COMPLETE_TASKS",
    "STOP_LIMIT_USAGE_AND_CANCEL_TASKS",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "STOP_LIMIT_USAGE_AND_COMPLETE_TASKS",
        "STOP_LIMIT_USAGE_AND_CANCEL_TASKS",
        "STOPPED",
    )
)


def serialize_json(value: QueueLimitAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> QueueLimitAssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown QueueLimitAssociationStatus value: {data!r}"
        )
    return cast(QueueLimitAssociationStatus, data)
