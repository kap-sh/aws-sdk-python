"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterBacktrackList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_cluster_backtrack

DBClusterBacktrackList: TypeAlias = list[
    "capo_rds.types.db_cluster_backtrack.DBClusterBacktrack"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterBacktrackList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_backtrack

    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_backtrack.serialize_query(
            item, pairs, f"{prefix}.DBClusterBacktrack.{n}"
        )


def deserialize_query(el: Element) -> DBClusterBacktrackList:
    import capo_rds.types.db_cluster_backtrack

    out: DBClusterBacktrackList = []
    for child in el.findall("DBClusterBacktrack"):
        out.append(capo_rds.types.db_cluster_backtrack.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBClusterBacktrackList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_backtrack

    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_backtrack.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBClusterBacktrackList:
    import capo_rds.types.db_cluster_backtrack

    out: DBClusterBacktrackList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_cluster_backtrack.deserialize_query(child))
    return out
