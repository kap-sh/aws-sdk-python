"""Generated from Smithy shape ``com.amazonaws.neptune#GlobalClustersMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.global_cluster_list
    import capo_neptune.types.string


class GlobalClustersMessage(TypedDict, closed=True):
    marker: NotRequired["capo_neptune.types.string.String"]
    """<p>A pagination token. If this parameter is returned in the response, more records are available, which can be retrieved by one or more additional calls to <code>DescribeGlobalClusters</code>.</p>"""
    global_clusters: NotRequired[
        "capo_neptune.types.global_cluster_list.GlobalClusterList"
    ]
    """<p>The list of global clusters and instances returned by this request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalClustersMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "global_clusters" in value:
        import capo_neptune.types.global_cluster_list

        capo_neptune.types.global_cluster_list.serialize_query(
            value["global_clusters"], pairs, f"{key_prefix}GlobalClusters"
        )


def deserialize_query(el: Element) -> GlobalClustersMessage:
    out: GlobalClustersMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_global_clusters = el.find("GlobalClusters")
    if child_global_clusters is not None:
        import capo_neptune.types.global_cluster_list

        out["global_clusters"] = (
            capo_neptune.types.global_cluster_list.deserialize_query(
                child_global_clusters
            )
        )
    return out
