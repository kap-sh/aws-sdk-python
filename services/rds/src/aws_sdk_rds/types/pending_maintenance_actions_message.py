"""Generated from Smithy shape ``com.amazonaws.rds#PendingMaintenanceActionsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.pending_maintenance_actions
    import aws_sdk_rds.types.string


class PendingMaintenanceActionsMessage(TypedDict):
    pending_maintenance_actions: NotRequired[
        "aws_sdk_rds.types.pending_maintenance_actions.PendingMaintenanceActions"
    ]
    """<p>A list of the pending maintenance actions for the resource.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribePendingMaintenanceActions</code> request. If this parameter is specified, the response includes only records beyond the marker, up to a number of records specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PendingMaintenanceActionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "pending_maintenance_actions" in value:
        import aws_sdk_rds.types.pending_maintenance_actions

        aws_sdk_rds.types.pending_maintenance_actions.serialize_query(
            value["pending_maintenance_actions"],
            pairs,
            f"{prefix}.PendingMaintenanceActions",
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> PendingMaintenanceActionsMessage:
    out: PendingMaintenanceActionsMessage = {}  # type: ignore[typeddict-item]
    child_pending_maintenance_actions = el.find("PendingMaintenanceActions")
    if child_pending_maintenance_actions is not None:
        import aws_sdk_rds.types.pending_maintenance_actions

        out["pending_maintenance_actions"] = (
            aws_sdk_rds.types.pending_maintenance_actions.deserialize_query(
                child_pending_maintenance_actions
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
