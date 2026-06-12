"""Generated from Smithy shape ``com.amazonaws.rds#PendingMaintenanceActions``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.resource_pending_maintenance_actions

PendingMaintenanceActions: TypeAlias = list[
    "aws_sdk_rds.types.resource_pending_maintenance_actions.ResourcePendingMaintenanceActions"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PendingMaintenanceActions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.resource_pending_maintenance_actions

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.resource_pending_maintenance_actions.serialize_query(
            item, pairs, f"{prefix}.ResourcePendingMaintenanceActions.{n}"
        )


def deserialize_query(el: Element) -> PendingMaintenanceActions:
    import aws_sdk_rds.types.resource_pending_maintenance_actions

    out: PendingMaintenanceActions = []
    for child in el.findall("ResourcePendingMaintenanceActions"):
        out.append(
            aws_sdk_rds.types.resource_pending_maintenance_actions.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: PendingMaintenanceActions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.resource_pending_maintenance_actions

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.resource_pending_maintenance_actions.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PendingMaintenanceActions:
    import aws_sdk_rds.types.resource_pending_maintenance_actions

    out: PendingMaintenanceActions = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_rds.types.resource_pending_maintenance_actions.deserialize_query(
                child
            )
        )
    return out
