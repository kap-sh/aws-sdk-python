"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

"""<p>The status of a notebook run in Amazon SageMaker Unified Studio.</p>"""
NotebookRunStatus: TypeAlias = Literal[
    "QUEUED",
    "STARTING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "STARTING",
        "RUNNING",
        "STOPPING",
        "STOPPED",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_json(value: NotebookRunStatus) -> str:
    return value


def deserialize_json(data: str) -> NotebookRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotebookRunStatus value: {data!r}")
    return cast(NotebookRunStatus, data)
