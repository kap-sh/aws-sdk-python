"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelArtifactMaxSizeUnitType``."""

from typing import Literal, TypeAlias, cast

TrainedModelArtifactMaxSizeUnitType: TypeAlias = Literal["GB",]


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelArtifactMaxSizeUnitType) -> str:
    return value


def deserialize_json(data: str) -> TrainedModelArtifactMaxSizeUnitType:
    return cast(TrainedModelArtifactMaxSizeUnitType, data)
