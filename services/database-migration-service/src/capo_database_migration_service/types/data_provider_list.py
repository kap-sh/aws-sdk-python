"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.data_provider

DataProviderList: TypeAlias = list[
    "capo_database_migration_service.types.data_provider.DataProvider"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataProviderList) -> list:
    import capo_database_migration_service.types.data_provider

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.data_provider.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataProviderList:
    import capo_database_migration_service.types.data_provider

    out: DataProviderList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.data_provider.deserialize_aws_json_1_1(
                item
            )
        )
    return out
