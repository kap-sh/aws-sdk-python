"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelExportsMaxSizeUnitType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

TrainedModelExportsMaxSizeUnitType: TypeAlias = Literal["GB",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("GB",))


def serialize_json(value: TrainedModelExportsMaxSizeUnitType) -> str:
    return value


def deserialize_json(data: str) -> TrainedModelExportsMaxSizeUnitType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TrainedModelExportsMaxSizeUnitType value: {data!r}"
        )
    return cast(TrainedModelExportsMaxSizeUnitType, data)
