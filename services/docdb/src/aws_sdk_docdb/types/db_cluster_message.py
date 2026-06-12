"""Generated from Smithy shape ``com.amazonaws.docdb#DBClusterMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.db_cluster_list
    import aws_sdk_docdb.types.string


class DBClusterMessage(TypedDict):
    marker: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_clusters: NotRequired["aws_sdk_docdb.types.db_cluster_list.DBClusterList"]
    """<p>A list of clusters.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_clusters" in value:
        import aws_sdk_docdb.types.db_cluster_list

        aws_sdk_docdb.types.db_cluster_list.serialize_query(
            value["db_clusters"], pairs, f"{prefix}.DBClusters"
        )


def deserialize_query(el: Element) -> DBClusterMessage:
    out: DBClusterMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_clusters = el.find("DBClusters")
    if child_db_clusters is not None:
        import aws_sdk_docdb.types.db_cluster_list

        out["db_clusters"] = aws_sdk_docdb.types.db_cluster_list.deserialize_query(
            child_db_clusters
        )
    return out
