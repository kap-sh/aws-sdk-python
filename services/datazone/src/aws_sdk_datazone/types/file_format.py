"""Generated from Smithy shape ``com.amazonaws.datazone#FileFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

"""<p>The file format for a notebook export in Amazon SageMaker Unified Studio.</p>"""
FileFormat: TypeAlias = Literal[
    "PDF",
    "IPYNB",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PDF",
        "IPYNB",
    )
)


def serialize_json(value: FileFormat) -> str:
    return value


def deserialize_json(data: str) -> FileFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileFormat value: {data!r}")
    return cast(FileFormat, data)
