"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_config

ReplicationConfigList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.replication_config.ReplicationConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationConfigList) -> list:
    import aws_sdk_database_migration_service.types.replication_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.replication_config.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationConfigList:
    import aws_sdk_database_migration_service.types.replication_config

    out: ReplicationConfigList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.replication_config.deserialize_aws_json_1_1(
                item
            )
        )
    return out
