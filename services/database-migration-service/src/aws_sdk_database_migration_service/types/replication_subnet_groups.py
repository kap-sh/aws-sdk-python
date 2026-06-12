"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationSubnetGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_subnet_group

ReplicationSubnetGroups: TypeAlias = list[
    "aws_sdk_database_migration_service.types.replication_subnet_group.ReplicationSubnetGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationSubnetGroups) -> list:
    import aws_sdk_database_migration_service.types.replication_subnet_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.replication_subnet_group.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationSubnetGroups:
    import aws_sdk_database_migration_service.types.replication_subnet_group

    out: ReplicationSubnetGroups = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.replication_subnet_group.deserialize_aws_json_1_1(
                item
            )
        )
    return out
