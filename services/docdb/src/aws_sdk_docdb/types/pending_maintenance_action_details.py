"""Generated from Smithy shape ``com.amazonaws.docdb#PendingMaintenanceActionDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.pending_maintenance_action

PendingMaintenanceActionDetails: TypeAlias = list[
    "aws_sdk_docdb.types.pending_maintenance_action.PendingMaintenanceAction"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PendingMaintenanceActionDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_docdb.types.pending_maintenance_action

    for n, item in enumerate(value, 1):
        aws_sdk_docdb.types.pending_maintenance_action.serialize_query(
            item, pairs, f"{prefix}.PendingMaintenanceAction.{n}"
        )


def deserialize_query(el: Element) -> PendingMaintenanceActionDetails:
    import aws_sdk_docdb.types.pending_maintenance_action

    out: PendingMaintenanceActionDetails = []
    for child in el.findall("PendingMaintenanceAction"):
        out.append(
            aws_sdk_docdb.types.pending_maintenance_action.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: PendingMaintenanceActionDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_docdb.types.pending_maintenance_action

    for n, item in enumerate(value, 1):
        aws_sdk_docdb.types.pending_maintenance_action.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> PendingMaintenanceActionDetails:
    import aws_sdk_docdb.types.pending_maintenance_action

    out: PendingMaintenanceActionDetails = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_docdb.types.pending_maintenance_action.deserialize_query(child)
        )
    return out
