"""Generated from Smithy shape ``com.amazonaws.securityhub#WorkflowStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

WorkflowStatus: TypeAlias = Literal[
    "NEW",
    "NOTIFIED",
    "RESOLVED",
    "SUPPRESSED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEW",
        "NOTIFIED",
        "RESOLVED",
        "SUPPRESSED",
    )
)


def serialize_json(value: WorkflowStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkflowStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkflowStatus value: {data!r}")
    return cast(WorkflowStatus, data)
