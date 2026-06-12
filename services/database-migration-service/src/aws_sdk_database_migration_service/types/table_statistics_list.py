"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TableStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.table_statistics

TableStatisticsList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.table_statistics.TableStatistics"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableStatisticsList) -> list:
    import aws_sdk_database_migration_service.types.table_statistics

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.table_statistics.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TableStatisticsList:
    import aws_sdk_database_migration_service.types.table_statistics

    out: TableStatisticsList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.table_statistics.deserialize_aws_json_1_1(
                item
            )
        )
    return out
