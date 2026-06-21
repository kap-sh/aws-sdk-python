"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelExportFileType``."""

from typing import Literal, TypeAlias, cast

TrainedModelExportFileType: TypeAlias = Literal[
    "MODEL",
    "OUTPUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelExportFileType) -> str:
    return value


def deserialize_json(data: str) -> TrainedModelExportFileType:
    return cast(TrainedModelExportFileType, data)
