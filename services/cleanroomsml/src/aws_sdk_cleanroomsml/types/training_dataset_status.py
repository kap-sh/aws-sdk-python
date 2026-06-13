"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainingDatasetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

TrainingDatasetStatus: TypeAlias = Literal["ACTIVE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ACTIVE",))


def serialize_json(value: TrainingDatasetStatus) -> str:
    return value


def deserialize_json(data: str) -> TrainingDatasetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrainingDatasetStatus value: {data!r}")
    return cast(TrainingDatasetStatus, data)
