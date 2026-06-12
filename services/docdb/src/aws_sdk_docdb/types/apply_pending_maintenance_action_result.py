"""Generated from Smithy shape ``com.amazonaws.docdb#ApplyPendingMaintenanceActionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.resource_pending_maintenance_actions


class ApplyPendingMaintenanceActionResult(TypedDict):
    resource_pending_maintenance_actions: NotRequired[
        "aws_sdk_docdb.types.resource_pending_maintenance_actions.ResourcePendingMaintenanceActions"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplyPendingMaintenanceActionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "resource_pending_maintenance_actions" in value:
        import aws_sdk_docdb.types.resource_pending_maintenance_actions

        aws_sdk_docdb.types.resource_pending_maintenance_actions.serialize_query(
            value["resource_pending_maintenance_actions"],
            pairs,
            f"{prefix}.ResourcePendingMaintenanceActions",
        )


def deserialize_query(el: Element) -> ApplyPendingMaintenanceActionResult:
    out: ApplyPendingMaintenanceActionResult = {}  # type: ignore[typeddict-item]
    child_resource_pending_maintenance_actions = el.find(
        "ResourcePendingMaintenanceActions"
    )
    if child_resource_pending_maintenance_actions is not None:
        import aws_sdk_docdb.types.resource_pending_maintenance_actions

        out["resource_pending_maintenance_actions"] = (
            aws_sdk_docdb.types.resource_pending_maintenance_actions.deserialize_query(
                child_resource_pending_maintenance_actions
            )
        )
    return out
