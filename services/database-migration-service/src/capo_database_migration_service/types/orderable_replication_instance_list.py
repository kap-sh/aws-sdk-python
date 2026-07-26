"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#OrderableReplicationInstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.orderable_replication_instance

OrderableReplicationInstanceList: TypeAlias = list[
    "capo_database_migration_service.types.orderable_replication_instance.OrderableReplicationInstance"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrderableReplicationInstanceList) -> list:
    import capo_database_migration_service.types.orderable_replication_instance

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.orderable_replication_instance.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrderableReplicationInstanceList:
    import capo_database_migration_service.types.orderable_replication_instance

    out: OrderableReplicationInstanceList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.orderable_replication_instance.deserialize_aws_json_1_1(
                item
            )
        )
    return out
