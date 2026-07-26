"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#PendingMaintenanceActionDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.pending_maintenance_action

PendingMaintenanceActionDetails: TypeAlias = list[
    "capo_database_migration_service.types.pending_maintenance_action.PendingMaintenanceAction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingMaintenanceActionDetails) -> list:
    import capo_database_migration_service.types.pending_maintenance_action

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.pending_maintenance_action.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PendingMaintenanceActionDetails:
    import capo_database_migration_service.types.pending_maintenance_action

    out: PendingMaintenanceActionDetails = []
    for item in data:
        out.append(
            capo_database_migration_service.types.pending_maintenance_action.deserialize_aws_json_1_1(
                item
            )
        )
    return out
