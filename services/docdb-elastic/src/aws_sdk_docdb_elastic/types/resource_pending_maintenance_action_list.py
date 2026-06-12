"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ResourcePendingMaintenanceActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.resource_pending_maintenance_action

ResourcePendingMaintenanceActionList: TypeAlias = list[
    "aws_sdk_docdb_elastic.types.resource_pending_maintenance_action.ResourcePendingMaintenanceAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePendingMaintenanceActionList) -> list:
    import aws_sdk_docdb_elastic.types.resource_pending_maintenance_action

    out: list = []
    for item in value:
        out.append(
            aws_sdk_docdb_elastic.types.resource_pending_maintenance_action.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResourcePendingMaintenanceActionList:
    import aws_sdk_docdb_elastic.types.resource_pending_maintenance_action

    out: ResourcePendingMaintenanceActionList = []
    for item in data:
        out.append(
            aws_sdk_docdb_elastic.types.resource_pending_maintenance_action.deserialize_json(
                item
            )
        )
    return out
