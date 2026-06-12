"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartMetadataModelImportMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean
    import aws_sdk_database_migration_service.types.migration_project_identifier
    import aws_sdk_database_migration_service.types.origin_type_value
    import aws_sdk_database_migration_service.types.string


class StartMetadataModelImportMessage(TypedDict):
    migration_project_identifier: "aws_sdk_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    selection_rules: "aws_sdk_database_migration_service.types.string.String"
    """<p>A value that specifies the database objects to import.</p>"""
    origin: "aws_sdk_database_migration_service.types.origin_type_value.OriginTypeValue"
    """<p>Whether to load metadata to the source or target database.</p>"""
    refresh: "aws_sdk_database_migration_service.types.boolean.Boolean"
    """<p>If <code>true</code>, DMS loads metadata for the specified objects from the source database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMetadataModelImportMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["SelectionRules"] = value["selection_rules"]
    import aws_sdk_database_migration_service.types.origin_type_value

    out["Origin"] = (
        aws_sdk_database_migration_service.types.origin_type_value.serialize_aws_json_1_1(
            value["origin"]
        )
    )
    out["Refresh"] = value.get("refresh", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMetadataModelImportMessage:
    out: StartMetadataModelImportMessage = {}  # type: ignore[typeddict-item]
    if "MigrationProjectIdentifier" in data:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "StartMetadataModelImportMessage.migration_project_identifier required"
        )
    if "SelectionRules" in data:
        out["selection_rules"] = data["SelectionRules"]
    else:
        raise DeserializationError(
            "StartMetadataModelImportMessage.selection_rules required"
        )
    if "Origin" in data:
        import aws_sdk_database_migration_service.types.origin_type_value

        out["origin"] = (
            aws_sdk_database_migration_service.types.origin_type_value.deserialize_aws_json_1_1(
                data["Origin"]
            )
        )
    else:
        raise DeserializationError("StartMetadataModelImportMessage.origin required")
    if "Refresh" in data:
        out["refresh"] = data["Refresh"]
    else:
        out["refresh"] = False
    return out
