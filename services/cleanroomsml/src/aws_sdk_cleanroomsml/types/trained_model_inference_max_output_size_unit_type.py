"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelInferenceMaxOutputSizeUnitType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

TrainedModelInferenceMaxOutputSizeUnitType: TypeAlias = Literal["GB",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("GB",))


def serialize_json(value: TrainedModelInferenceMaxOutputSizeUnitType) -> str:
    return value


def deserialize_json(data: str) -> TrainedModelInferenceMaxOutputSizeUnitType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TrainedModelInferenceMaxOutputSizeUnitType value: {data!r}"
        )
    return cast(TrainedModelInferenceMaxOutputSizeUnitType, data)
