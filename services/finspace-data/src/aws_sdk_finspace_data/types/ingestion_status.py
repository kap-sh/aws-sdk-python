"""Generated from Smithy shape ``com.amazonaws.finspacedata#IngestionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace_data.errors import DeserializationError

"""Status of the ingestion process returned from scheduler service."""
IngestionStatus: TypeAlias = Literal[
    "PENDING",
    "FAILED",
    "SUCCESS",
    "RUNNING",
    "STOP_REQUESTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "FAILED",
        "SUCCESS",
        "RUNNING",
        "STOP_REQUESTED",
    )
)


def serialize_json(value: IngestionStatus) -> str:
    return value


def deserialize_json(data: str) -> IngestionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngestionStatus value: {data!r}")
    return cast(IngestionStatus, data)
