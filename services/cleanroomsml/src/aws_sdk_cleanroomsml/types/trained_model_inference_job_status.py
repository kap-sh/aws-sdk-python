"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelInferenceJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

TrainedModelInferenceJobStatus: TypeAlias = Literal[
    "CREATE_PENDING",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "ACTIVE",
    "CANCEL_PENDING",
    "CANCEL_IN_PROGRESS",
    "CANCEL_FAILED",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_PENDING",
        "CREATE_IN_PROGRESS",
        "CREATE_FAILED",
        "ACTIVE",
        "CANCEL_PENDING",
        "CANCEL_IN_PROGRESS",
        "CANCEL_FAILED",
        "INACTIVE",
    )
)


def serialize_json(value: TrainedModelInferenceJobStatus) -> str:
    return value


def deserialize_json(data: str) -> TrainedModelInferenceJobStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TrainedModelInferenceJobStatus value: {data!r}"
        )
    return cast(TrainedModelInferenceJobStatus, data)
