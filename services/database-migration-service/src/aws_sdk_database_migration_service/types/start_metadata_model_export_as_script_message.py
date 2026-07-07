"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartMetadataModelExportAsScriptMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.migration_project_identifier
    import aws_sdk_database_migration_service.types.origin_type_value
    import aws_sdk_database_migration_service.types.string


class StartMetadataModelExportAsScriptMessage(TypedDict, closed=True):
    migration_project_identifier: "aws_sdk_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    selection_rules: "aws_sdk_database_migration_service.types.string.String"
    """<p>A value that specifies the database objects to export.</p>"""
    origin: "aws_sdk_database_migration_service.types.origin_type_value.OriginTypeValue"
    """<p>Whether to export the metadata model from the source or the target.</p>"""
    file_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The name of the model file to create in the Amazon S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMetadataModelExportAsScriptMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["SelectionRules"] = value["selection_rules"]
    import aws_sdk_database_migration_service.types.origin_type_value

    out["Origin"] = (
        aws_sdk_database_migration_service.types.origin_type_value.serialize_aws_json_1_1(
            value["origin"]
        )
    )
    if "file_name" in value:
        out["FileName"] = value["file_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMetadataModelExportAsScriptMessage:
    out: StartMetadataModelExportAsScriptMessage = {}  # type: ignore[typeddict-item]
    if "MigrationProjectIdentifier" in data:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "StartMetadataModelExportAsScriptMessage.migration_project_identifier required"
        )
    if "SelectionRules" in data:
        out["selection_rules"] = data["SelectionRules"]
    else:
        raise DeserializationError(
            "StartMetadataModelExportAsScriptMessage.selection_rules required"
        )
    if "Origin" in data:
        import aws_sdk_database_migration_service.types.origin_type_value

        out["origin"] = (
            aws_sdk_database_migration_service.types.origin_type_value.deserialize_aws_json_1_1(
                data["Origin"]
            )
        )
    else:
        raise DeserializationError(
            "StartMetadataModelExportAsScriptMessage.origin required"
        )
    if "FileName" in data:
        out["file_name"] = data["FileName"]
    return out
