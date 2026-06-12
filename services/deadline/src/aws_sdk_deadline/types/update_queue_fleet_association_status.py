"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateQueueFleetAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

UpdateQueueFleetAssociationStatus: TypeAlias = Literal[
    "ACTIVE",
    "STOP_SCHEDULING_AND_COMPLETE_TASKS",
    "STOP_SCHEDULING_AND_CANCEL_TASKS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "STOP_SCHEDULING_AND_COMPLETE_TASKS",
        "STOP_SCHEDULING_AND_CANCEL_TASKS",
    )
)


def serialize_json(value: UpdateQueueFleetAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> UpdateQueueFleetAssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UpdateQueueFleetAssociationStatus value: {data!r}"
        )
    return cast(UpdateQueueFleetAssociationStatus, data)
