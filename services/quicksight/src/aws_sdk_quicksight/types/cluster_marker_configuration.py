"""Generated from Smithy shape ``com.amazonaws.quicksight#ClusterMarkerConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.cluster_marker


class ClusterMarkerConfiguration(TypedDict):
    cluster_marker: NotRequired["aws_sdk_quicksight.types.cluster_marker.ClusterMarker"]
    """<p>The cluster marker that is a part of the cluster marker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterMarkerConfiguration) -> dict:
    out: dict = {}
    if "cluster_marker" in value:
        import aws_sdk_quicksight.types.cluster_marker

        out["ClusterMarker"] = aws_sdk_quicksight.types.cluster_marker.serialize_json(
            value["cluster_marker"]
        )
    return out


def deserialize_json(data: dict) -> ClusterMarkerConfiguration:
    out: ClusterMarkerConfiguration = {}  # type: ignore[typeddict-item]
    if "ClusterMarker" in data:
        import aws_sdk_quicksight.types.cluster_marker

        out["cluster_marker"] = (
            aws_sdk_quicksight.types.cluster_marker.deserialize_json(
                data["ClusterMarker"]
            )
        )
    return out
