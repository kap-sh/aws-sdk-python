"""Generated from Smithy shape ``com.amazonaws.redshift#TableRestoreStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.table_restore_status

TableRestoreStatusList: TypeAlias = list[
    "capo_redshift.types.table_restore_status.TableRestoreStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TableRestoreStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.table_restore_status

    for n, item in enumerate(value, 1):
        capo_redshift.types.table_restore_status.serialize_query(
            item, pairs, f"{prefix}.TableRestoreStatus.{n}"
        )


def deserialize_query(el: Element) -> TableRestoreStatusList:
    import capo_redshift.types.table_restore_status

    out: TableRestoreStatusList = []
    for child in el.findall("TableRestoreStatus"):
        out.append(capo_redshift.types.table_restore_status.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TableRestoreStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.table_restore_status

    for n, item in enumerate(value, 1):
        capo_redshift.types.table_restore_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TableRestoreStatusList:
    import capo_redshift.types.table_restore_status

    out: TableRestoreStatusList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.table_restore_status.deserialize_query(child))
    return out
