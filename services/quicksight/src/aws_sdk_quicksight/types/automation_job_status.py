"""Generated from Smithy shape ``com.amazonaws.quicksight#AutomationJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AutomationJobStatus: TypeAlias = Literal[
    "FAILED",
    "RUNNING",
    "SUCCEEDED",
    "QUEUED",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "RUNNING",
        "SUCCEEDED",
        "QUEUED",
        "STOPPED",
    )
)


def serialize_json(value: AutomationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutomationJobStatus value: {data!r}")
    return cast(AutomationJobStatus, data)
