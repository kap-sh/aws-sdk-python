"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataProviderDescriptorDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.data_provider_descriptor_definition

DataProviderDescriptorDefinitionList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.data_provider_descriptor_definition.DataProviderDescriptorDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataProviderDescriptorDefinitionList) -> list:
    import aws_sdk_database_migration_service.types.data_provider_descriptor_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.data_provider_descriptor_definition.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataProviderDescriptorDefinitionList:
    import aws_sdk_database_migration_service.types.data_provider_descriptor_definition

    out: DataProviderDescriptorDefinitionList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.data_provider_descriptor_definition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
