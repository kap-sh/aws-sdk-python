"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportFormat``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

ExportFormat: TypeAlias = Literal[
    "DYNAMODB_JSON",
    "ION",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DYNAMODB_JSON",
        "ION",
    )
)


def serialize_aws_json_1_0(value: ExportFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportFormat value: {data!r}")
    return cast(ExportFormat, data)
