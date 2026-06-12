"""Generated from Smithy shape ``com.amazonaws.securityhub#WorkflowState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

WorkflowState: TypeAlias = Literal[
    "NEW",
    "ASSIGNED",
    "IN_PROGRESS",
    "DEFERRED",
    "RESOLVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEW",
        "ASSIGNED",
        "IN_PROGRESS",
        "DEFERRED",
        "RESOLVED",
    )
)


def serialize_json(value: WorkflowState) -> str:
    return value


def deserialize_json(data: str) -> WorkflowState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkflowState value: {data!r}")
    return cast(WorkflowState, data)
