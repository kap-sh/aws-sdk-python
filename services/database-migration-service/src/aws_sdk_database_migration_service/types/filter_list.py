"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.filter

FilterList: TypeAlias = list["aws_sdk_database_migration_service.types.filter.Filter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterList) -> list:
    import aws_sdk_database_migration_service.types.filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FilterList:
    import aws_sdk_database_migration_service.types.filter

    out: FilterList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
