"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartReplicationTaskTypeValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

StartReplicationTaskTypeValue: TypeAlias = Literal[
    "start-replication",
    "resume-processing",
    "reload-target",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "start-replication",
        "resume-processing",
        "reload-target",
    )
)


def serialize_aws_json_1_1(value: StartReplicationTaskTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StartReplicationTaskTypeValue:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StartReplicationTaskTypeValue value: {data!r}"
        )
    return cast(StartReplicationTaskTypeValue, data)
