"""Generated from Smithy shape ``com.amazonaws.rds#GlobalClustersMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.global_cluster_list
    import aws_sdk_rds.types.string


class GlobalClustersMessage(TypedDict):
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeGlobalClusters</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    global_clusters: NotRequired[
        "aws_sdk_rds.types.global_cluster_list.GlobalClusterList"
    ]
    """<p>The list of global clusters returned by this request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalClustersMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "global_clusters" in value:
        import aws_sdk_rds.types.global_cluster_list

        aws_sdk_rds.types.global_cluster_list.serialize_query(
            value["global_clusters"], pairs, f"{prefix}.GlobalClusters"
        )


def deserialize_query(el: Element) -> GlobalClustersMessage:
    out: GlobalClustersMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_global_clusters = el.find("GlobalClusters")
    if child_global_clusters is not None:
        import aws_sdk_rds.types.global_cluster_list

        out["global_clusters"] = (
            aws_sdk_rds.types.global_cluster_list.deserialize_query(
                child_global_clusters
            )
        )
    return out
