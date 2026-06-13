"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelExportFileType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

TrainedModelExportFileType: TypeAlias = Literal[
    "MODEL",
    "OUTPUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MODEL",
        "OUTPUT",
    )
)


def serialize_json(value: TrainedModelExportFileType) -> str:
    return value


def deserialize_json(data: str) -> TrainedModelExportFileType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TrainedModelExportFileType value: {data!r}"
        )
    return cast(TrainedModelExportFileType, data)
