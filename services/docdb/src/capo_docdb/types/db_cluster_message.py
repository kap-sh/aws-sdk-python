"""Generated from Smithy shape ``com.amazonaws.docdb#DBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.db_cluster_list
    import capo_docdb.types.string


class DBClusterMessage(TypedDict, closed=True):
    marker: NotRequired["capo_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_clusters: NotRequired["capo_docdb.types.db_cluster_list.DBClusterList"]
    """<p>A list of clusters.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "db_clusters" in value:
        import capo_docdb.types.db_cluster_list

        capo_docdb.types.db_cluster_list.serialize_query(
            value["db_clusters"], pairs, f"{key_prefix}DBClusters"
        )


def deserialize_query(el: Element) -> DBClusterMessage:
    out: DBClusterMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_clusters = el.find("DBClusters")
    if child_db_clusters is not None:
        import capo_docdb.types.db_cluster_list

        out["db_clusters"] = capo_docdb.types.db_cluster_list.deserialize_query(
            child_db_clusters
        )
    return out
