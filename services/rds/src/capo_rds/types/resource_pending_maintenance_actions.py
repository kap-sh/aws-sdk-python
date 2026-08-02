"""Generated from Smithy shape ``com.amazonaws.rds#ResourcePendingMaintenanceActions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.pending_maintenance_action_details
    import capo_rds.types.string


class ResourcePendingMaintenanceActions(TypedDict, closed=True):
    resource_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN of the resource that has pending maintenance actions.</p>"""
    pending_maintenance_action_details: NotRequired[
        "capo_rds.types.pending_maintenance_action_details.PendingMaintenanceActionDetails"
    ]
    """<p>A list that provides details about the pending maintenance actions for the resource.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourcePendingMaintenanceActions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_identifier" in value:
        pairs.append(
            (f"{key_prefix}ResourceIdentifier", str(value["resource_identifier"]))
        )
    if "pending_maintenance_action_details" in value:
        import capo_rds.types.pending_maintenance_action_details

        capo_rds.types.pending_maintenance_action_details.serialize_query(
            value["pending_maintenance_action_details"],
            pairs,
            f"{key_prefix}PendingMaintenanceActionDetails",
        )


def deserialize_query(el: Element) -> ResourcePendingMaintenanceActions:
    out: ResourcePendingMaintenanceActions = {}  # type: ignore[typeddict-item]
    child_resource_identifier = el.find("ResourceIdentifier")
    if child_resource_identifier is not None:
        out["resource_identifier"] = str(child_resource_identifier.text or "")
    child_pending_maintenance_action_details = el.find(
        "PendingMaintenanceActionDetails"
    )
    if child_pending_maintenance_action_details is not None:
        import capo_rds.types.pending_maintenance_action_details

        out["pending_maintenance_action_details"] = (
            capo_rds.types.pending_maintenance_action_details.deserialize_query(
                child_pending_maintenance_action_details
            )
        )
    return out
