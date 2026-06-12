"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_cluster_list
    import aws_sdk_rds.types.string


class DBClusterMessage(TypedDict):
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A pagination token that can be used in a later <code>DescribeDBClusters</code> request.</p>"""
    db_clusters: NotRequired["aws_sdk_rds.types.db_cluster_list.DBClusterList"]
    """<p>Contains a list of DB clusters for the user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_clusters" in value:
        import aws_sdk_rds.types.db_cluster_list

        aws_sdk_rds.types.db_cluster_list.serialize_query(
            value["db_clusters"], pairs, f"{prefix}.DBClusters"
        )


def deserialize_query(el: Element) -> DBClusterMessage:
    out: DBClusterMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_clusters = el.find("DBClusters")
    if child_db_clusters is not None:
        import aws_sdk_rds.types.db_cluster_list

        out["db_clusters"] = aws_sdk_rds.types.db_cluster_list.deserialize_query(
            child_db_clusters
        )
    return out
