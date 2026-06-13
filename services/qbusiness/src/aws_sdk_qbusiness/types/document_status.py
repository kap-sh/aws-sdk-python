"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

DocumentStatus: TypeAlias = Literal[
    "RECEIVED",
    "PROCESSING",
    "INDEXED",
    "UPDATED",
    "FAILED",
    "DELETING",
    "DELETED",
    "DOCUMENT_FAILED_TO_INDEX",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RECEIVED",
        "PROCESSING",
        "INDEXED",
        "UPDATED",
        "FAILED",
        "DELETING",
        "DELETED",
        "DOCUMENT_FAILED_TO_INDEX",
    )
)


def serialize_json(value: DocumentStatus) -> str:
    return value


def deserialize_json(data: str) -> DocumentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentStatus value: {data!r}")
    return cast(DocumentStatus, data)
