"""Generated from Smithy shape ``com.amazonaws.deadline#QueueFleetAssociationStatus``."""

from typing import Literal, TypeAlias, cast

QueueFleetAssociationStatus: TypeAlias = Literal[
    "ACTIVE",
    "STOP_SCHEDULING_AND_COMPLETE_TASKS",
    "STOP_SCHEDULING_AND_CANCEL_TASKS",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueueFleetAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> QueueFleetAssociationStatus:
    return cast(QueueFleetAssociationStatus, data)
