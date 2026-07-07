"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#GetTargetSelectionRulesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.migration_project_identifier
    import aws_sdk_database_migration_service.types.string


class GetTargetSelectionRulesMessage(TypedDict, closed=True):
    migration_project_identifier: "aws_sdk_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    selection_rules: "aws_sdk_database_migration_service.types.string.String"
    """<p>The JSON string representing the source selection rules for conversion. Selection rules must contain only supported metadata model types. For more information, see Selection Rules in the DMS User Guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTargetSelectionRulesMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["SelectionRules"] = value["selection_rules"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTargetSelectionRulesMessage:
    out: GetTargetSelectionRulesMessage = {}  # type: ignore[typeddict-item]
    if "MigrationProjectIdentifier" in data:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "GetTargetSelectionRulesMessage.migration_project_identifier required"
        )
    if "SelectionRules" in data:
        out["selection_rules"] = data["SelectionRules"]
    else:
        raise DeserializationError(
            "GetTargetSelectionRulesMessage.selection_rules required"
        )
    return out
