"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#PluginNameValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

PluginNameValue: TypeAlias = Literal[
    "no-preference",
    "test-decoding",
    "pglogical",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "no-preference",
        "test-decoding",
        "pglogical",
    )
)


def serialize_aws_json_1_1(value: PluginNameValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PluginNameValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PluginNameValue value: {data!r}")
    return cast(PluginNameValue, data)
