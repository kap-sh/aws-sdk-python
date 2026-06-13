"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainingInputMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

TrainingInputMode: TypeAlias = Literal[
    "File",
    "FastFile",
    "Pipe",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "File",
        "FastFile",
        "Pipe",
    )
)


def serialize_json(value: TrainingInputMode) -> str:
    return value


def deserialize_json(data: str) -> TrainingInputMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrainingInputMode value: {data!r}")
    return cast(TrainingInputMode, data)
