"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DatePartitionDelimiterValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

DatePartitionDelimiterValue: TypeAlias = Literal[
    "SLASH",
    "UNDERSCORE",
    "DASH",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SLASH",
        "UNDERSCORE",
        "DASH",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: DatePartitionDelimiterValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatePartitionDelimiterValue:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DatePartitionDelimiterValue value: {data!r}"
        )
    return cast(DatePartitionDelimiterValue, data)
