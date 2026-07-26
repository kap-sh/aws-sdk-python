"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribePendingMaintenanceActionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.pending_maintenance_actions
    import capo_database_migration_service.types.string


class DescribePendingMaintenanceActionsResponse(TypedDict, closed=True):
    pending_maintenance_actions: NotRequired[
        "capo_database_migration_service.types.pending_maintenance_actions.PendingMaintenanceActions"
    ]
    """<p>The pending maintenance action.</p>"""
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePendingMaintenanceActionsResponse) -> dict:
    out: dict = {}
    if "pending_maintenance_actions" in value:
        import capo_database_migration_service.types.pending_maintenance_actions

        out["PendingMaintenanceActions"] = (
            capo_database_migration_service.types.pending_maintenance_actions.serialize_aws_json_1_1(
                value["pending_maintenance_actions"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePendingMaintenanceActionsResponse:
    out: DescribePendingMaintenanceActionsResponse = {}  # type: ignore[typeddict-item]
    if "PendingMaintenanceActions" in data:
        import capo_database_migration_service.types.pending_maintenance_actions

        out["pending_maintenance_actions"] = (
            capo_database_migration_service.types.pending_maintenance_actions.deserialize_aws_json_1_1(
                data["PendingMaintenanceActions"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
