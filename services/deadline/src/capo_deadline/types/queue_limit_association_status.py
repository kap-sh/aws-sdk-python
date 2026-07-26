"""Generated from Smithy shape ``com.amazonaws.deadline#QueueLimitAssociationStatus``."""

from typing import Literal, TypeAlias, cast

QueueLimitAssociationStatus: TypeAlias = Literal[
    "ACTIVE",
    "STOP_LIMIT_USAGE_AND_COMPLETE_TASKS",
    "STOP_LIMIT_USAGE_AND_CANCEL_TASKS",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueueLimitAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> QueueLimitAssociationStatus:
    return cast(QueueLimitAssociationStatus, data)
