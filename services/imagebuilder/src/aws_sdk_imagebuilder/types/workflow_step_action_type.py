"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowStepActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

WorkflowStepActionType: TypeAlias = Literal[
    "RESUME",
    "STOP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESUME",
        "STOP",
    )
)


def serialize_json(value: WorkflowStepActionType) -> str:
    return value


def deserialize_json(data: str) -> WorkflowStepActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkflowStepActionType value: {data!r}")
    return cast(WorkflowStepActionType, data)
