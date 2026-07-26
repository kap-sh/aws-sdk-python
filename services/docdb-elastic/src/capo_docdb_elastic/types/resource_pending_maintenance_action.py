"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ResourcePendingMaintenanceAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.pending_maintenance_action_details_list


class ResourcePendingMaintenanceAction(TypedDict, closed=True):
    resource_arn: NotRequired["str"]
    """<p>The Amazon DocumentDB Amazon Resource Name (ARN) of the resource to which the pending maintenance action applies.</p>"""
    pending_maintenance_action_details: NotRequired[
        "capo_docdb_elastic.types.pending_maintenance_action_details_list.PendingMaintenanceActionDetailsList"
    ]
    """<p>Provides information about a pending maintenance action for a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePendingMaintenanceAction) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "pending_maintenance_action_details" in value:
        import capo_docdb_elastic.types.pending_maintenance_action_details_list

        out["pendingMaintenanceActionDetails"] = (
            capo_docdb_elastic.types.pending_maintenance_action_details_list.serialize_json(
                value["pending_maintenance_action_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourcePendingMaintenanceAction:
    out: ResourcePendingMaintenanceAction = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "pendingMaintenanceActionDetails" in data:
        import capo_docdb_elastic.types.pending_maintenance_action_details_list

        out["pending_maintenance_action_details"] = (
            capo_docdb_elastic.types.pending_maintenance_action_details_list.deserialize_json(
                data["pendingMaintenanceActionDetails"]
            )
        )
    return out
