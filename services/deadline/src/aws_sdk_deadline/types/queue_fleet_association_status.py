"""Generated from Smithy shape ``com.amazonaws.deadline#QueueFleetAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

QueueFleetAssociationStatus: TypeAlias = Literal[
    "ACTIVE",
    "STOP_SCHEDULING_AND_COMPLETE_TASKS",
    "STOP_SCHEDULING_AND_CANCEL_TASKS",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "STOP_SCHEDULING_AND_COMPLETE_TASKS",
        "STOP_SCHEDULING_AND_CANCEL_TASKS",
        "STOPPED",
    )
)


def serialize_json(value: QueueFleetAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> QueueFleetAssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown QueueFleetAssociationStatus value: {data!r}"
        )
    return cast(QueueFleetAssociationStatus, data)
