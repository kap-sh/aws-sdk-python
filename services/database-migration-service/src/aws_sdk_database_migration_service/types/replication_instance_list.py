"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationInstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_instance

ReplicationInstanceList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.replication_instance.ReplicationInstance"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationInstanceList) -> list:
    import aws_sdk_database_migration_service.types.replication_instance

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.replication_instance.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationInstanceList:
    import aws_sdk_database_migration_service.types.replication_instance

    out: ReplicationInstanceList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.replication_instance.deserialize_aws_json_1_1(
                item
            )
        )
    return out
