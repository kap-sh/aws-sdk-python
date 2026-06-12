"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyConversionConfigurationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.migration_project_identifier
    import aws_sdk_database_migration_service.types.string


class ModifyConversionConfigurationMessage(TypedDict):
    migration_project_identifier: "aws_sdk_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    conversion_configuration: "aws_sdk_database_migration_service.types.string.String"
    """<p>The new conversion configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyConversionConfigurationMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["ConversionConfiguration"] = value["conversion_configuration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyConversionConfigurationMessage:
    out: ModifyConversionConfigurationMessage = {}  # type: ignore[typeddict-item]
    if "MigrationProjectIdentifier" in data:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "ModifyConversionConfigurationMessage.migration_project_identifier required"
        )
    if "ConversionConfiguration" in data:
        out["conversion_configuration"] = data["ConversionConfiguration"]
    else:
        raise DeserializationError(
            "ModifyConversionConfigurationMessage.conversion_configuration required"
        )
    return out
