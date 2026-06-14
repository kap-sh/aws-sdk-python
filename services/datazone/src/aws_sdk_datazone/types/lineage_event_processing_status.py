"""Generated from Smithy shape ``com.amazonaws.datazone#LineageEventProcessingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

LineageEventProcessingStatus: TypeAlias = Literal[
    "REQUESTED",
    "PROCESSING",
    "SUCCESS",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUESTED",
        "PROCESSING",
        "SUCCESS",
        "FAILED",
    )
)


def serialize_json(value: LineageEventProcessingStatus) -> str:
    return value


def deserialize_json(data: str) -> LineageEventProcessingStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LineageEventProcessingStatus value: {data!r}"
        )
    return cast(LineageEventProcessingStatus, data)
