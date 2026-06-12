"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MetadataModelReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.metadata_model_reference

MetadataModelReferenceList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.metadata_model_reference.MetadataModelReference"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetadataModelReferenceList) -> list:
    import aws_sdk_database_migration_service.types.metadata_model_reference

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.metadata_model_reference.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MetadataModelReferenceList:
    import aws_sdk_database_migration_service.types.metadata_model_reference

    out: MetadataModelReferenceList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.metadata_model_reference.deserialize_aws_json_1_1(
                item
            )
        )
    return out
