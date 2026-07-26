"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#PendingMaintenanceActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.resource_pending_maintenance_actions

PendingMaintenanceActions: TypeAlias = list[
    "capo_database_migration_service.types.resource_pending_maintenance_actions.ResourcePendingMaintenanceActions"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingMaintenanceActions) -> list:
    import capo_database_migration_service.types.resource_pending_maintenance_actions

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.resource_pending_maintenance_actions.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PendingMaintenanceActions:
    import capo_database_migration_service.types.resource_pending_maintenance_actions

    out: PendingMaintenanceActions = []
    for item in data:
        out.append(
            capo_database_migration_service.types.resource_pending_maintenance_actions.deserialize_aws_json_1_1(
                item
            )
        )
    return out
