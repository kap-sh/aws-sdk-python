"""Generated from Smithy shape ``com.amazonaws.redshift#TrackListMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string
    import capo_redshift.types.track_list


class TrackListMessage(TypedDict, closed=True):
    maintenance_tracks: NotRequired["capo_redshift.types.track_list.TrackList"]
    """<p>A list of maintenance tracks output by the <code>DescribeClusterTracks</code> operation. </p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>The starting point to return a set of response tracklist records. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TrackListMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "maintenance_tracks" in value:
        import capo_redshift.types.track_list

        capo_redshift.types.track_list.serialize_query(
            value["maintenance_tracks"], pairs, f"{prefix}.MaintenanceTracks"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> TrackListMessage:
    out: TrackListMessage = {}  # type: ignore[typeddict-item]
    child_maintenance_tracks = el.find("MaintenanceTracks")
    if child_maintenance_tracks is not None:
        import capo_redshift.types.track_list

        out["maintenance_tracks"] = capo_redshift.types.track_list.deserialize_query(
            child_maintenance_tracks
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
