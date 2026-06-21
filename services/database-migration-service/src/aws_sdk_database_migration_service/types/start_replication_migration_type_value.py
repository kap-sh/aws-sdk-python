"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartReplicationMigrationTypeValue``."""

from typing import Literal, TypeAlias, cast

StartReplicationMigrationTypeValue: TypeAlias = Literal[
    "reload-target",
    "resume-processing",
    "start-replication",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReplicationMigrationTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StartReplicationMigrationTypeValue:
    return cast(StartReplicationMigrationTypeValue, data)
