"""Generated from Smithy shape ``com.amazonaws.docdb#FailoverDBClusterResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.db_cluster


class FailoverDBClusterResult(TypedDict, closed=True):
    db_cluster: NotRequired["capo_docdb.types.db_cluster.DBCluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: FailoverDBClusterResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster" in value:
        import capo_docdb.types.db_cluster

        capo_docdb.types.db_cluster.serialize_query(
            value["db_cluster"], pairs, f"{prefix}.DBCluster"
        )


def deserialize_query(el: Element) -> FailoverDBClusterResult:
    out: FailoverDBClusterResult = {}  # type: ignore[typeddict-item]
    child_db_cluster = el.find("DBCluster")
    if child_db_cluster is not None:
        import capo_docdb.types.db_cluster

        out["db_cluster"] = capo_docdb.types.db_cluster.deserialize_query(
            child_db_cluster
        )
    return out
