"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelStatus``."""

from typing import Literal, TypeAlias, cast

TrainedModelStatus: TypeAlias = Literal[
    "CREATE_PENDING",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "ACTIVE",
    "DELETE_PENDING",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
    "INACTIVE",
    "CANCEL_PENDING",
    "CANCEL_IN_PROGRESS",
    "CANCEL_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelStatus) -> str:
    return value


def deserialize_json(data: str) -> TrainedModelStatus:
    return cast(TrainedModelStatus, data)
