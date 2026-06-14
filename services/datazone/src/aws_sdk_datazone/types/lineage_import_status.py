"""Generated from Smithy shape ``com.amazonaws.datazone#LineageImportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

LineageImportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESS",
    "FAILED",
    "PARTIALLY_SUCCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCESS",
        "FAILED",
        "PARTIALLY_SUCCEEDED",
    )
)


def serialize_json(value: LineageImportStatus) -> str:
    return value


def deserialize_json(data: str) -> LineageImportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LineageImportStatus value: {data!r}")
    return cast(LineageImportStatus, data)
