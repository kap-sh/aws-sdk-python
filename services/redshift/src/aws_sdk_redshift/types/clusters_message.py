"""Generated from Smithy shape ``com.amazonaws.redshift#ClustersMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.cluster_list
    import aws_sdk_redshift.types.string


class ClustersMessage(TypedDict):
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    clusters: NotRequired["aws_sdk_redshift.types.cluster_list.ClusterList"]
    """<p>A list of <code>Cluster</code> objects, where each object describes one cluster. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClustersMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "clusters" in value:
        import aws_sdk_redshift.types.cluster_list

        aws_sdk_redshift.types.cluster_list.serialize_query(
            value["clusters"], pairs, f"{prefix}.Clusters"
        )


def deserialize_query(el: Element) -> ClustersMessage:
    out: ClustersMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_clusters = el.find("Clusters")
    if child_clusters is not None:
        import aws_sdk_redshift.types.cluster_list

        out["clusters"] = aws_sdk_redshift.types.cluster_list.deserialize_query(
            child_clusters
        )
    return out
