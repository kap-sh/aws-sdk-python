"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartMetadataModelImportMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean
    import capo_database_migration_service.types.migration_project_identifier
    import capo_database_migration_service.types.origin_type_value
    import capo_database_migration_service.types.string


class StartMetadataModelImportMessage(TypedDict, closed=True):
    migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    selection_rules: "capo_database_migration_service.types.string.String"
    """<p>A value that specifies the database objects to import.</p>"""
    origin: "capo_database_migration_service.types.origin_type_value.OriginTypeValue"
    """<p>Whether to load metadata to the source or target database.</p>"""
    refresh: "capo_database_migration_service.types.boolean.Boolean"
    """<p>If <code>true</code>, DMS loads metadata for the specified objects from the source database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMetadataModelImportMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["SelectionRules"] = value["selection_rules"]
    import capo_database_migration_service.types.origin_type_value

    out["Origin"] = (
        capo_database_migration_service.types.origin_type_value.serialize_aws_json_1_1(
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
        import capo_database_migration_service.types.origin_type_value

        out["origin"] = (
            capo_database_migration_service.types.origin_type_value.deserialize_aws_json_1_1(
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
