"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainingDatasetStatus``."""

from typing import Literal, TypeAlias, cast

TrainingDatasetStatus: TypeAlias = Literal["ACTIVE",]


# --- restJson1 ser/de ---
def serialize_json(value: TrainingDatasetStatus) -> str:
    return value


def deserialize_json(data: str) -> TrainingDatasetStatus:
    return cast(TrainingDatasetStatus, data)
