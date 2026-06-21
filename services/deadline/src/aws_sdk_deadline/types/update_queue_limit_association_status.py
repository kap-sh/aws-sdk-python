"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateQueueLimitAssociationStatus``."""

from typing import Literal, TypeAlias, cast

UpdateQueueLimitAssociationStatus: TypeAlias = Literal[
    "ACTIVE",
    "STOP_LIMIT_USAGE_AND_COMPLETE_TASKS",
    "STOP_LIMIT_USAGE_AND_CANCEL_TASKS",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueLimitAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> UpdateQueueLimitAssociationStatus:
    return cast(UpdateQueueLimitAssociationStatus, data)
