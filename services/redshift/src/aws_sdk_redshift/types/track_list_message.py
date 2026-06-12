"""Generated from Smithy shape ``com.amazonaws.redshift#TrackListMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.track_list


class TrackListMessage(TypedDict):
    maintenance_tracks: NotRequired["aws_sdk_redshift.types.track_list.TrackList"]
    """<p>A list of maintenance tracks output by the <code>DescribeClusterTracks</code> operation. </p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The starting point to return a set of response tracklist records. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TrackListMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "maintenance_tracks" in value:
        import aws_sdk_redshift.types.track_list

        aws_sdk_redshift.types.track_list.serialize_query(
            value["maintenance_tracks"], pairs, f"{prefix}.MaintenanceTracks"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> TrackListMessage:
    out: TrackListMessage = {}  # type: ignore[typeddict-item]
    child_maintenance_tracks = el.find("MaintenanceTracks")
    if child_maintenance_tracks is not None:
        import aws_sdk_redshift.types.track_list

        out["maintenance_tracks"] = aws_sdk_redshift.types.track_list.deserialize_query(
            child_maintenance_tracks
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
