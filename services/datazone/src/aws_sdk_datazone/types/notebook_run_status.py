"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookRunStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: NotebookRunStatus) -> str:
    return value


def deserialize_json(data: str) -> NotebookRunStatus:
    return cast(NotebookRunStatus, data)
