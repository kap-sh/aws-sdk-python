"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartMetadataModelConversionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.migration_project_identifier
    import capo_database_migration_service.types.string


class StartMetadataModelConversionMessage(TypedDict, closed=True):
    migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    selection_rules: "capo_database_migration_service.types.string.String"
    """<p>A value that specifies the database objects to convert.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMetadataModelConversionMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["SelectionRules"] = value["selection_rules"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMetadataModelConversionMessage:
    out: StartMetadataModelConversionMessage = {}  # type: ignore[typeddict-item]
    if "MigrationProjectIdentifier" in data:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "StartMetadataModelConversionMessage.migration_project_identifier required"
        )
    if "SelectionRules" in data:
        out["selection_rules"] = data["SelectionRules"]
    else:
        raise DeserializationError(
            "StartMetadataModelConversionMessage.selection_rules required"
        )
    return out
