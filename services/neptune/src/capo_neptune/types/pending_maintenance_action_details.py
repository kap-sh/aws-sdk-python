"""Generated from Smithy shape ``com.amazonaws.neptune#PendingMaintenanceActionDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.pending_maintenance_action

PendingMaintenanceActionDetails: TypeAlias = list[
    "capo_neptune.types.pending_maintenance_action.PendingMaintenanceAction"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PendingMaintenanceActionDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.pending_maintenance_action

    for n, item in enumerate(value, 1):
        capo_neptune.types.pending_maintenance_action.serialize_query(
            item, pairs, f"{prefix}.PendingMaintenanceAction.{n}"
        )


def deserialize_query(el: Element) -> PendingMaintenanceActionDetails:
    import capo_neptune.types.pending_maintenance_action

    out: PendingMaintenanceActionDetails = []
    for child in el.findall("PendingMaintenanceAction"):
        out.append(
            capo_neptune.types.pending_maintenance_action.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: PendingMaintenanceActionDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.pending_maintenance_action

    for n, item in enumerate(value, 1):
        capo_neptune.types.pending_maintenance_action.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> PendingMaintenanceActionDetails:
    import capo_neptune.types.pending_maintenance_action

    out: PendingMaintenanceActionDetails = []
    for child in parent.findall(tag):
        out.append(
            capo_neptune.types.pending_maintenance_action.deserialize_query(child)
        )
    return out
