"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterOptionGroupMemberships``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_cluster_option_group_status

DBClusterOptionGroupMemberships: TypeAlias = list[
    "capo_rds.types.db_cluster_option_group_status.DBClusterOptionGroupStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterOptionGroupMemberships, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_option_group_status

    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_option_group_status.serialize_query(
            item, pairs, f"{prefix}.DBClusterOptionGroup.{n}"
        )


def deserialize_query(el: Element) -> DBClusterOptionGroupMemberships:
    import capo_rds.types.db_cluster_option_group_status

    out: DBClusterOptionGroupMemberships = []
    for child in el.findall("DBClusterOptionGroup"):
        out.append(
            capo_rds.types.db_cluster_option_group_status.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: DBClusterOptionGroupMemberships, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_option_group_status

    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_option_group_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> DBClusterOptionGroupMemberships:
    import capo_rds.types.db_cluster_option_group_status

    out: DBClusterOptionGroupMemberships = []
    for child in parent.findall(tag):
        out.append(
            capo_rds.types.db_cluster_option_group_status.deserialize_query(child)
        )
    return out
