"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CompressionTypeValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

CompressionTypeValue: TypeAlias = Literal[
    "none",
    "gzip",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "none",
        "gzip",
    )
)


def serialize_aws_json_1_1(value: CompressionTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompressionTypeValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CompressionTypeValue value: {data!r}")
    return cast(CompressionTypeValue, data)
