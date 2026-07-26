"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookExportStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a notebook export in Amazon SageMaker Unified Studio.</p>"""
NotebookExportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotebookExportStatus) -> str:
    return value


def deserialize_json(data: str) -> NotebookExportStatus:
    return cast(NotebookExportStatus, data)
