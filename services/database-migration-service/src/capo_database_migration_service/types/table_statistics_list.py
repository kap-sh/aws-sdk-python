"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TableStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.table_statistics

TableStatisticsList: TypeAlias = list[
    "capo_database_migration_service.types.table_statistics.TableStatistics"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableStatisticsList) -> list:
    import capo_database_migration_service.types.table_statistics

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.table_statistics.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TableStatisticsList:
    import capo_database_migration_service.types.table_statistics

    out: TableStatisticsList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.table_statistics.deserialize_aws_json_1_1(
                item
            )
        )
    return out
