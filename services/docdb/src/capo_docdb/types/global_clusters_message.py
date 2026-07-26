"""Generated from Smithy shape ``com.amazonaws.docdb#GlobalClustersMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.global_cluster_list
    import capo_docdb.types.string


class GlobalClustersMessage(TypedDict, closed=True):
    marker: NotRequired["capo_docdb.types.string.String"]
    """<p></p>"""
    global_clusters: NotRequired[
        "capo_docdb.types.global_cluster_list.GlobalClusterList"
    ]
    """<p></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalClustersMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "global_clusters" in value:
        import capo_docdb.types.global_cluster_list

        capo_docdb.types.global_cluster_list.serialize_query(
            value["global_clusters"], pairs, f"{prefix}.GlobalClusters"
        )


def deserialize_query(el: Element) -> GlobalClustersMessage:
    out: GlobalClustersMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_global_clusters = el.find("GlobalClusters")
    if child_global_clusters is not None:
        import capo_docdb.types.global_cluster_list

        out["global_clusters"] = capo_docdb.types.global_cluster_list.deserialize_query(
            child_global_clusters
        )
    return out
