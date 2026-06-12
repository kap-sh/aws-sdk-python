"""Generated from Smithy shape ``com.amazonaws.cognitosync#BulkPublishStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_sync.errors import DeserializationError

BulkPublishStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_STARTED",
        "IN_PROGRESS",
        "FAILED",
        "SUCCEEDED",
    )
)


def serialize_json(value: BulkPublishStatus) -> str:
    return value


def deserialize_json(data: str) -> BulkPublishStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BulkPublishStatus value: {data!r}")
    return cast(BulkPublishStatus, data)
