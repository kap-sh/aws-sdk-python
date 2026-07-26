"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelInferenceMaxOutputSizeUnitType``."""

from typing import Literal, TypeAlias, cast

TrainedModelInferenceMaxOutputSizeUnitType: TypeAlias = Literal["GB",]


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelInferenceMaxOutputSizeUnitType) -> str:
    return value


def deserialize_json(data: str) -> TrainedModelInferenceMaxOutputSizeUnitType:
    return cast(TrainedModelInferenceMaxOutputSizeUnitType, data)
