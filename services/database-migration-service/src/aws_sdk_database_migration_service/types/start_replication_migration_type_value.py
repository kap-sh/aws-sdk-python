"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartReplicationMigrationTypeValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

StartReplicationMigrationTypeValue: TypeAlias = Literal[
    "reload-target",
    "resume-processing",
    "start-replication",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "reload-target",
        "resume-processing",
        "start-replication",
    )
)


def serialize_aws_json_1_1(value: StartReplicationMigrationTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StartReplicationMigrationTypeValue:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StartReplicationMigrationTypeValue value: {data!r}"
        )
    return cast(StartReplicationMigrationTypeValue, data)
