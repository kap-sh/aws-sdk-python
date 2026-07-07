"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ApplyPendingMaintenanceActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.resource_pending_maintenance_actions


class ApplyPendingMaintenanceActionResponse(TypedDict, closed=True):
    resource_pending_maintenance_actions: NotRequired[
        "aws_sdk_database_migration_service.types.resource_pending_maintenance_actions.ResourcePendingMaintenanceActions"
    ]
    """<p>The DMS resource that the pending maintenance action will be applied to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplyPendingMaintenanceActionResponse) -> dict:
    out: dict = {}
    if "resource_pending_maintenance_actions" in value:
        import aws_sdk_database_migration_service.types.resource_pending_maintenance_actions

        out["ResourcePendingMaintenanceActions"] = (
            aws_sdk_database_migration_service.types.resource_pending_maintenance_actions.serialize_aws_json_1_1(
                value["resource_pending_maintenance_actions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplyPendingMaintenanceActionResponse:
    out: ApplyPendingMaintenanceActionResponse = {}  # type: ignore[typeddict-item]
    if "ResourcePendingMaintenanceActions" in data:
        import aws_sdk_database_migration_service.types.resource_pending_maintenance_actions

        out["resource_pending_maintenance_actions"] = (
            aws_sdk_database_migration_service.types.resource_pending_maintenance_actions.deserialize_aws_json_1_1(
                data["ResourcePendingMaintenanceActions"]
            )
        )
    return out
