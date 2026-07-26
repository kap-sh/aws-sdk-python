"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.replication

ReplicationList: TypeAlias = list[
    "capo_database_migration_service.types.replication.Replication"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationList) -> list:
    import capo_database_migration_service.types.replication

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.replication.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationList:
    import capo_database_migration_service.types.replication

    out: ReplicationList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.replication.deserialize_aws_json_1_1(
                item
            )
        )
    return out
