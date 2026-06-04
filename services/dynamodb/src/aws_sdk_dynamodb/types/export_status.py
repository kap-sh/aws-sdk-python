"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

ExportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_aws_json_1_0(value: ExportStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportStatus value: {data!r}")
    return cast(ExportStatus, data)
