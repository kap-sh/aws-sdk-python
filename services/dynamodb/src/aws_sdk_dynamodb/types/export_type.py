"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

ExportType: TypeAlias = Literal[
    "FULL_EXPORT",
    "INCREMENTAL_EXPORT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL_EXPORT",
        "INCREMENTAL_EXPORT",
    )
)


def serialize_aws_json_1_0(value: ExportType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportType value: {data!r}")
    return cast(ExportType, data)
