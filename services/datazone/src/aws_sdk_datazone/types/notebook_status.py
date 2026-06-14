"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

"""<p>The status of a notebook in Amazon SageMaker Unified Studio.</p>"""
NotebookStatus: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "ARCHIVED",
    )
)


def serialize_json(value: NotebookStatus) -> str:
    return value


def deserialize_json(data: str) -> NotebookStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotebookStatus value: {data!r}")
    return cast(NotebookStatus, data)
