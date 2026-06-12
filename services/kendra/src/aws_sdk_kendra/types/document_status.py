"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

DocumentStatus: TypeAlias = Literal[
    "NOT_FOUND",
    "PROCESSING",
    "INDEXED",
    "UPDATED",
    "FAILED",
    "UPDATE_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_FOUND",
        "PROCESSING",
        "INDEXED",
        "UPDATED",
        "FAILED",
        "UPDATE_FAILED",
    )
)


def serialize_aws_json_1_1(value: DocumentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentStatus value: {data!r}")
    return cast(DocumentStatus, data)
