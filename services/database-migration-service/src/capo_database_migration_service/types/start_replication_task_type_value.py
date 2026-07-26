"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartReplicationTaskTypeValue``."""

from typing import Literal, TypeAlias, cast

StartReplicationTaskTypeValue: TypeAlias = Literal[
    "start-replication",
    "resume-processing",
    "reload-target",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReplicationTaskTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StartReplicationTaskTypeValue:
    return cast(StartReplicationTaskTypeValue, data)
