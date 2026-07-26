"""Generated from Smithy shape ``com.amazonaws.neptune#DBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.db_cluster_list
    import capo_neptune.types.string


class DBClusterMessage(TypedDict, closed=True):
    marker: NotRequired["capo_neptune.types.string.String"]
    """<p>A pagination token that can be used in a subsequent DescribeDBClusters request.</p>"""
    db_clusters: NotRequired["capo_neptune.types.db_cluster_list.DBClusterList"]
    """<p>Contains a list of DB clusters for the user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_clusters" in value:
        import capo_neptune.types.db_cluster_list

        capo_neptune.types.db_cluster_list.serialize_query(
            value["db_clusters"], pairs, f"{prefix}.DBClusters"
        )


def deserialize_query(el: Element) -> DBClusterMessage:
    out: DBClusterMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_clusters = el.find("DBClusters")
    if child_db_clusters is not None:
        import capo_neptune.types.db_cluster_list

        out["db_clusters"] = capo_neptune.types.db_cluster_list.deserialize_query(
            child_db_clusters
        )
    return out
