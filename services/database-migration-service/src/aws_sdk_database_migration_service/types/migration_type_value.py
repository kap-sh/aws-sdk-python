"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MigrationTypeValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

MigrationTypeValue: TypeAlias = Literal[
    "full-load",
    "cdc",
    "full-load-and-cdc",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "full-load",
        "cdc",
        "full-load-and-cdc",
    )
)


def serialize_aws_json_1_1(value: MigrationTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MigrationTypeValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MigrationTypeValue value: {data!r}")
    return cast(MigrationTypeValue, data)
