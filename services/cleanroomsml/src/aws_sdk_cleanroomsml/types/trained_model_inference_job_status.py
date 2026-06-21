"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelInferenceJobStatus``."""

from typing import Literal, TypeAlias, cast

TrainedModelInferenceJobStatus: TypeAlias = Literal[
    "CREATE_PENDING",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "ACTIVE",
    "CANCEL_PENDING",
    "CANCEL_IN_PROGRESS",
    "CANCEL_FAILED",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelInferenceJobStatus) -> str:
    return value


def deserialize_json(data: str) -> TrainedModelInferenceJobStatus:
    return cast(TrainedModelInferenceJobStatus, data)
