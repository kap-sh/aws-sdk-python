"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterAssociatedRoles``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_cluster_associated_role

DBClusterAssociatedRoles: TypeAlias = list[
    "capo_rds.types.db_cluster_associated_role.DBClusterAssociatedRole"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterAssociatedRoles, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_associated_role

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_associated_role.serialize_query(
            item, pairs, f"{prefix}.DBClusterAssociatedRole.{n}"
        )


def deserialize_query(el: Element) -> DBClusterAssociatedRoles:
    import capo_rds.types.db_cluster_associated_role

    out: DBClusterAssociatedRoles = []
    for child in el.findall("DBClusterAssociatedRole"):
        out.append(capo_rds.types.db_cluster_associated_role.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBClusterAssociatedRoles, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_associated_role

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_associated_role.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBClusterAssociatedRoles:
    import capo_rds.types.db_cluster_associated_role

    out: DBClusterAssociatedRoles = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_cluster_associated_role.deserialize_query(child))
    return out
