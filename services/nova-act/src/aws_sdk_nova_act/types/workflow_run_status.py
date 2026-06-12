"""Generated from Smithy shape ``com.amazonaws.novaact#WorkflowRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_nova_act.errors import DeserializationError

WorkflowRunStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "TIMED_OUT",
        "DELETING",
    )
)


def serialize_json(value: WorkflowRunStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkflowRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkflowRunStatus value: {data!r}")
    return cast(WorkflowRunStatus, data)
