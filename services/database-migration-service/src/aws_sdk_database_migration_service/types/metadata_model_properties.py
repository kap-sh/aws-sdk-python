"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MetadataModelProperties``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_database_migration_service.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.statement_properties


class _MetadataModelProperties_StatementProperties(TypedDict, closed=True):
    StatementProperties: "aws_sdk_database_migration_service.types.statement_properties.StatementProperties"


MetadataModelProperties: TypeAlias = _MetadataModelProperties_StatementProperties


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetadataModelProperties) -> dict:
    if "StatementProperties" in value:
        import aws_sdk_database_migration_service.types.statement_properties

        return {
            "StatementProperties": aws_sdk_database_migration_service.types.statement_properties.serialize_aws_json_1_1(
                value["StatementProperties"]
            )
        }
    else:
        raise SerializationError("MetadataModelProperties: no variant present")


def deserialize_aws_json_1_1(data: dict) -> MetadataModelProperties:
    if "StatementProperties" in data:
        import aws_sdk_database_migration_service.types.statement_properties

        return {
            "StatementProperties": aws_sdk_database_migration_service.types.statement_properties.deserialize_aws_json_1_1(
                data["StatementProperties"]
            )
        }
    else:
        raise DeserializationError("MetadataModelProperties: no recognized variant key")
