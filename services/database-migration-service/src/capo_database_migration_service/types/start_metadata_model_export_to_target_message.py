"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartMetadataModelExportToTargetMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.migration_project_identifier
    import capo_database_migration_service.types.string


class StartMetadataModelExportToTargetMessage(TypedDict, closed=True):
    migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    selection_rules: "capo_database_migration_service.types.string.String"
    """<p>A value that specifies the database objects to export.</p>"""
    overwrite_extension_pack: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Whether to overwrite the migration project extension pack. An extension pack is an add-on module that emulates functions present in a source database that are required when converting objects to the target database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMetadataModelExportToTargetMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["SelectionRules"] = value["selection_rules"]
    if "overwrite_extension_pack" in value:
        out["OverwriteExtensionPack"] = value["overwrite_extension_pack"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMetadataModelExportToTargetMessage:
    out: StartMetadataModelExportToTargetMessage = {}  # type: ignore[typeddict-item]
    if "MigrationProjectIdentifier" in data:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "StartMetadataModelExportToTargetMessage.migration_project_identifier required"
        )
    if "SelectionRules" in data:
        out["selection_rules"] = data["SelectionRules"]
    else:
        raise DeserializationError(
            "StartMetadataModelExportToTargetMessage.selection_rules required"
        )
    if "OverwriteExtensionPack" in data:
        out["overwrite_extension_pack"] = data["OverwriteExtensionPack"]
    return out
