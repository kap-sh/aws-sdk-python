"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ExportFilesStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gameliftstreams.errors import DeserializationError

ExportFilesStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "PENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "FAILED",
        "PENDING",
    )
)


def serialize_json(value: ExportFilesStatus) -> str:
    return value


def deserialize_json(data: str) -> ExportFilesStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportFilesStatus value: {data!r}")
    return cast(ExportFilesStatus, data)
