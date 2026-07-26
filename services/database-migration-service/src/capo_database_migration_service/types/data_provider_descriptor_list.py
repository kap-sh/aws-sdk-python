"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataProviderDescriptorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.data_provider_descriptor

DataProviderDescriptorList: TypeAlias = list[
    "capo_database_migration_service.types.data_provider_descriptor.DataProviderDescriptor"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataProviderDescriptorList) -> list:
    import capo_database_migration_service.types.data_provider_descriptor

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.data_provider_descriptor.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataProviderDescriptorList:
    import capo_database_migration_service.types.data_provider_descriptor

    out: DataProviderDescriptorList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.data_provider_descriptor.deserialize_aws_json_1_1(
                item
            )
        )
    return out
