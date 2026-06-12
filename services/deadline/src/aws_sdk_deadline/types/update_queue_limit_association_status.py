"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateQueueLimitAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

UpdateQueueLimitAssociationStatus: TypeAlias = Literal[
    "ACTIVE",
    "STOP_LIMIT_USAGE_AND_COMPLETE_TASKS",
    "STOP_LIMIT_USAGE_AND_CANCEL_TASKS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "STOP_LIMIT_USAGE_AND_COMPLETE_TASKS",
        "STOP_LIMIT_USAGE_AND_CANCEL_TASKS",
    )
)


def serialize_json(value: UpdateQueueLimitAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> UpdateQueueLimitAssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UpdateQueueLimitAssociationStatus value: {data!r}"
        )
    return cast(UpdateQueueLimitAssociationStatus, data)
