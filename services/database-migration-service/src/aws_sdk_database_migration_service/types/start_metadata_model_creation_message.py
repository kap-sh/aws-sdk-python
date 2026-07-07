"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartMetadataModelCreationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.metadata_model_properties
    import aws_sdk_database_migration_service.types.migration_project_identifier
    import aws_sdk_database_migration_service.types.string


class StartMetadataModelCreationMessage(TypedDict, closed=True):
    migration_project_identifier: "aws_sdk_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    selection_rules: "aws_sdk_database_migration_service.types.string.String"
    """<p>The JSON string that specifies the location where the metadata model will be created. Selection rules must specify a single schema. For more information, see Selection Rules in the DMS User Guide.</p>"""
    metadata_model_name: "aws_sdk_database_migration_service.types.string.String"
    """<p>The name of the metadata model.</p>"""
    properties: "aws_sdk_database_migration_service.types.metadata_model_properties.MetadataModelProperties"
    """<p>The properties of metadata model in JSON format. This object is a Union. Only one member of this object can be specified or returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMetadataModelCreationMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["SelectionRules"] = value["selection_rules"]
    out["MetadataModelName"] = value["metadata_model_name"]
    import aws_sdk_database_migration_service.types.metadata_model_properties

    out["Properties"] = (
        aws_sdk_database_migration_service.types.metadata_model_properties.serialize_aws_json_1_1(
            value["properties"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMetadataModelCreationMessage:
    out: StartMetadataModelCreationMessage = {}  # type: ignore[typeddict-item]
    if "MigrationProjectIdentifier" in data:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "StartMetadataModelCreationMessage.migration_project_identifier required"
        )
    if "SelectionRules" in data:
        out["selection_rules"] = data["SelectionRules"]
    else:
        raise DeserializationError(
            "StartMetadataModelCreationMessage.selection_rules required"
        )
    if "MetadataModelName" in data:
        out["metadata_model_name"] = data["MetadataModelName"]
    else:
        raise DeserializationError(
            "StartMetadataModelCreationMessage.metadata_model_name required"
        )
    if "Properties" in data:
        import aws_sdk_database_migration_service.types.metadata_model_properties

        out["properties"] = (
            aws_sdk_database_migration_service.types.metadata_model_properties.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    else:
        raise DeserializationError(
            "StartMetadataModelCreationMessage.properties required"
        )
    return out
