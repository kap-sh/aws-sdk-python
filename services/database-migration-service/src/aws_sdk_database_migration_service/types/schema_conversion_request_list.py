"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SchemaConversionRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.schema_conversion_request

SchemaConversionRequestList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.schema_conversion_request.SchemaConversionRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaConversionRequestList) -> list:
    import aws_sdk_database_migration_service.types.schema_conversion_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.schema_conversion_request.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SchemaConversionRequestList:
    import aws_sdk_database_migration_service.types.schema_conversion_request

    out: SchemaConversionRequestList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.schema_conversion_request.deserialize_aws_json_1_1(
                item
            )
        )
    return out
