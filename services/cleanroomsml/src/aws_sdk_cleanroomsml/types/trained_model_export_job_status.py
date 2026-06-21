"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelExportJobStatus``."""

from typing import Literal, TypeAlias, cast

TrainedModelExportJobStatus: TypeAlias = Literal[
    "CREATE_PENDING",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelExportJobStatus) -> str:
    return value


def deserialize_json(data: str) -> TrainedModelExportJobStatus:
    return cast(TrainedModelExportJobStatus, data)
