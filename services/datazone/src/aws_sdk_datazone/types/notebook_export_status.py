"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookExportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

"""<p>The status of a notebook export in Amazon SageMaker Unified Studio.</p>"""
NotebookExportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_json(value: NotebookExportStatus) -> str:
    return value


def deserialize_json(data: str) -> NotebookExportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotebookExportStatus value: {data!r}")
    return cast(NotebookExportStatus, data)
