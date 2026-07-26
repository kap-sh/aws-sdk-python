"""Generated from Smithy shape ``com.amazonaws.redshift#DeferredMaintenanceWindowsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.deferred_maintenance_window

DeferredMaintenanceWindowsList: TypeAlias = list[
    "capo_redshift.types.deferred_maintenance_window.DeferredMaintenanceWindow"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DeferredMaintenanceWindowsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.deferred_maintenance_window

    for n, item in enumerate(value, 1):
        capo_redshift.types.deferred_maintenance_window.serialize_query(
            item, pairs, f"{prefix}.DeferredMaintenanceWindow.{n}"
        )


def deserialize_query(el: Element) -> DeferredMaintenanceWindowsList:
    import capo_redshift.types.deferred_maintenance_window

    out: DeferredMaintenanceWindowsList = []
    for child in el.findall("DeferredMaintenanceWindow"):
        out.append(
            capo_redshift.types.deferred_maintenance_window.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: DeferredMaintenanceWindowsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.deferred_maintenance_window

    for n, item in enumerate(value, 1):
        capo_redshift.types.deferred_maintenance_window.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DeferredMaintenanceWindowsList:
    import capo_redshift.types.deferred_maintenance_window

    out: DeferredMaintenanceWindowsList = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.deferred_maintenance_window.deserialize_query(child)
        )
    return out
