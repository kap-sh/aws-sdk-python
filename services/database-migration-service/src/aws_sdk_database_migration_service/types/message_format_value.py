"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MessageFormatValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

MessageFormatValue: TypeAlias = Literal[
    "json",
    "json-unformatted",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "json",
        "json-unformatted",
    )
)


def serialize_aws_json_1_1(value: MessageFormatValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MessageFormatValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageFormatValue value: {data!r}")
    return cast(MessageFormatValue, data)
