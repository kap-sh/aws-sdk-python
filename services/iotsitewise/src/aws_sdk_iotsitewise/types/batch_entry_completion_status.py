"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchEntryCompletionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

BatchEntryCompletionStatus: TypeAlias = Literal[
    "SUCCESS",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "ERROR",
    )
)


def serialize_json(value: BatchEntryCompletionStatus) -> str:
    return value


def deserialize_json(data: str) -> BatchEntryCompletionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchEntryCompletionStatus value: {data!r}"
        )
    return cast(BatchEntryCompletionStatus, data)
