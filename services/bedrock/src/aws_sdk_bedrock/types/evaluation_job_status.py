"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

EvaluationJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
    "Deleting",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
        "Stopping",
        "Stopped",
        "Deleting",
    )
)


def serialize_json(value: EvaluationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationJobStatus value: {data!r}")
    return cast(EvaluationJobStatus, data)
