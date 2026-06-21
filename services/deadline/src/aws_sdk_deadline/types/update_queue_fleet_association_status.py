"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateQueueFleetAssociationStatus``."""

from typing import Literal, TypeAlias, cast

UpdateQueueFleetAssociationStatus: TypeAlias = Literal[
    "ACTIVE",
    "STOP_SCHEDULING_AND_COMPLETE_TASKS",
    "STOP_SCHEDULING_AND_CANCEL_TASKS",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueFleetAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> UpdateQueueFleetAssociationStatus:
    return cast(UpdateQueueFleetAssociationStatus, data)
