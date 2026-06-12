"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication

ReplicationList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.replication.Replication"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationList) -> list:
    import aws_sdk_database_migration_service.types.replication

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.replication.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationList:
    import aws_sdk_database_migration_service.types.replication

    out: ReplicationList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.replication.deserialize_aws_json_1_1(
                item
            )
        )
    return out
