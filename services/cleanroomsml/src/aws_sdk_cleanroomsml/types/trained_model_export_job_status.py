"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelExportJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

TrainedModelExportJobStatus: TypeAlias = Literal[
    "CREATE_PENDING",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "ACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_PENDING",
        "CREATE_IN_PROGRESS",
        "CREATE_FAILED",
        "ACTIVE",
    )
)


def serialize_json(value: TrainedModelExportJobStatus) -> str:
    return value


def deserialize_json(data: str) -> TrainedModelExportJobStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TrainedModelExportJobStatus value: {data!r}"
        )
    return cast(TrainedModelExportJobStatus, data)
