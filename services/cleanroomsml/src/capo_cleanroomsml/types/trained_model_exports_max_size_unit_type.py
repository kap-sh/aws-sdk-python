"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelExportsMaxSizeUnitType``."""

from typing import Literal, TypeAlias, cast

TrainedModelExportsMaxSizeUnitType: TypeAlias = Literal["GB",]


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelExportsMaxSizeUnitType) -> str:
    return value


def deserialize_json(data: str) -> TrainedModelExportsMaxSizeUnitType:
    return cast(TrainedModelExportsMaxSizeUnitType, data)
