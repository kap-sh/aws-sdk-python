"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a notebook in Amazon SageMaker Unified Studio.</p>"""
NotebookStatus: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotebookStatus) -> str:
    return value


def deserialize_json(data: str) -> NotebookStatus:
    return cast(NotebookStatus, data)
