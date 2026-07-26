"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationTableStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.table_statistics

ReplicationTableStatisticsList: TypeAlias = list[
    "capo_database_migration_service.types.table_statistics.TableStatistics"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationTableStatisticsList) -> list:
    import capo_database_migration_service.types.table_statistics

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.table_statistics.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationTableStatisticsList:
    import capo_database_migration_service.types.table_statistics

    out: ReplicationTableStatisticsList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.table_statistics.deserialize_aws_json_1_1(
                item
            )
        )
    return out
