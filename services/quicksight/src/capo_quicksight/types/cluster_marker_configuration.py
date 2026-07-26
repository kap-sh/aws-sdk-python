"""Generated from Smithy shape ``com.amazonaws.quicksight#ClusterMarkerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.cluster_marker


class ClusterMarkerConfiguration(TypedDict, closed=True):
    cluster_marker: NotRequired["capo_quicksight.types.cluster_marker.ClusterMarker"]
    """<p>The cluster marker that is a part of the cluster marker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterMarkerConfiguration) -> dict:
    out: dict = {}
    if "cluster_marker" in value:
        import capo_quicksight.types.cluster_marker

        out["ClusterMarker"] = capo_quicksight.types.cluster_marker.serialize_json(
            value["cluster_marker"]
        )
    return out


def deserialize_json(data: dict) -> ClusterMarkerConfiguration:
    out: ClusterMarkerConfiguration = {}  # type: ignore[typeddict-item]
    if "ClusterMarker" in data:
        import capo_quicksight.types.cluster_marker

        out["cluster_marker"] = capo_quicksight.types.cluster_marker.deserialize_json(
            data["ClusterMarker"]
        )
    return out
