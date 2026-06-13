"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelArtifactMaxSizeUnitType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

TrainedModelArtifactMaxSizeUnitType: TypeAlias = Literal["GB",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("GB",))


def serialize_json(value: TrainedModelArtifactMaxSizeUnitType) -> str:
    return value


def deserialize_json(data: str) -> TrainedModelArtifactMaxSizeUnitType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TrainedModelArtifactMaxSizeUnitType value: {data!r}"
        )
    return cast(TrainedModelArtifactMaxSizeUnitType, data)
