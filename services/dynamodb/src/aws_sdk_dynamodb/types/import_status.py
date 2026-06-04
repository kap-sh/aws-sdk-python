"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

ImportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "CANCELLING",
    "CANCELLED",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETED",
        "CANCELLING",
        "CANCELLED",
        "FAILED",
    )
)


def serialize_aws_json_1_0(value: ImportStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ImportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportStatus value: {data!r}")
    return cast(ImportStatus, data)
