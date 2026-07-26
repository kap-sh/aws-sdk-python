"""Generated from Smithy shape ``com.amazonaws.docdbelastic#PendingMaintenanceActionDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_docdb_elastic.types.pending_maintenance_action_details

PendingMaintenanceActionDetailsList: TypeAlias = list[
    "capo_docdb_elastic.types.pending_maintenance_action_details.PendingMaintenanceActionDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: PendingMaintenanceActionDetailsList) -> list:
    import capo_docdb_elastic.types.pending_maintenance_action_details

    out: list = []
    for item in value:
        out.append(
            capo_docdb_elastic.types.pending_maintenance_action_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PendingMaintenanceActionDetailsList:
    import capo_docdb_elastic.types.pending_maintenance_action_details

    out: PendingMaintenanceActionDetailsList = []
    for item in data:
        out.append(
            capo_docdb_elastic.types.pending_maintenance_action_details.deserialize_json(
                item
            )
        )
    return out
