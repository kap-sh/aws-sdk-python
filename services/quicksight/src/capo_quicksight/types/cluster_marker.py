"""Generated from Smithy shape ``com.amazonaws.quicksight#ClusterMarker``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.simple_cluster_marker


class ClusterMarker(TypedDict, closed=True):
    simple_cluster_marker: NotRequired[
        "capo_quicksight.types.simple_cluster_marker.SimpleClusterMarker"
    ]
    """<p>The simple cluster marker of the cluster marker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterMarker) -> dict:
    out: dict = {}
    if "simple_cluster_marker" in value:
        import capo_quicksight.types.simple_cluster_marker

        out["SimpleClusterMarker"] = (
            capo_quicksight.types.simple_cluster_marker.serialize_json(
                value["simple_cluster_marker"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClusterMarker:
    out: ClusterMarker = {}  # type: ignore[typeddict-item]
    if "SimpleClusterMarker" in data:
        import capo_quicksight.types.simple_cluster_marker

        out["simple_cluster_marker"] = (
            capo_quicksight.types.simple_cluster_marker.deserialize_json(
                data["SimpleClusterMarker"]
            )
        )
    return out
