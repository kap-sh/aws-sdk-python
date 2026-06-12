"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ResourcePendingMaintenanceAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.pending_maintenance_action_details_list


class ResourcePendingMaintenanceAction(TypedDict):
    resource_arn: NotRequired["str"]
    """<p>The Amazon DocumentDB Amazon Resource Name (ARN) of the resource to which the pending maintenance action applies.</p>"""
    pending_maintenance_action_details: NotRequired[
        "aws_sdk_docdb_elastic.types.pending_maintenance_action_details_list.PendingMaintenanceActionDetailsList"
    ]
    """<p>Provides information about a pending maintenance action for a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePendingMaintenanceAction) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "pending_maintenance_action_details" in value:
        import aws_sdk_docdb_elastic.types.pending_maintenance_action_details_list

        out["pendingMaintenanceActionDetails"] = (
            aws_sdk_docdb_elastic.types.pending_maintenance_action_details_list.serialize_json(
                value["pending_maintenance_action_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourcePendingMaintenanceAction:
    out: ResourcePendingMaintenanceAction = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "pendingMaintenanceActionDetails" in data:
        import aws_sdk_docdb_elastic.types.pending_maintenance_action_details_list

        out["pending_maintenance_action_details"] = (
            aws_sdk_docdb_elastic.types.pending_maintenance_action_details_list.deserialize_json(
                data["pendingMaintenanceActionDetails"]
            )
        )
    return out
