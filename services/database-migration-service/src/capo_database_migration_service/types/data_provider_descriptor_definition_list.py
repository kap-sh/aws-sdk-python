"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataProviderDescriptorDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.data_provider_descriptor_definition

DataProviderDescriptorDefinitionList: TypeAlias = list[
    "capo_database_migration_service.types.data_provider_descriptor_definition.DataProviderDescriptorDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataProviderDescriptorDefinitionList) -> list:
    import capo_database_migration_service.types.data_provider_descriptor_definition

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.data_provider_descriptor_definition.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataProviderDescriptorDefinitionList:
    import capo_database_migration_service.types.data_provider_descriptor_definition

    out: DataProviderDescriptorDefinitionList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.data_provider_descriptor_definition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
