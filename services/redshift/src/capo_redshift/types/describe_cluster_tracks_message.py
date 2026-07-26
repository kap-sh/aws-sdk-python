"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeClusterTracksMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integer_optional
    import capo_redshift.types.string


class DescribeClusterTracksMessage(TypedDict, closed=True):
    maintenance_track_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the maintenance track. </p>"""
    max_records: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>An integer value for the maximum number of maintenance tracks to return.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <code>DescribeClusterTracks</code> request exceed the value specified in <code>MaxRecords</code>, Amazon Redshift returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeClusterTracksMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "maintenance_track_name" in value:
        pairs.append(
            (f"{prefix}.MaintenanceTrackName", str(value["maintenance_track_name"]))
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeClusterTracksMessage:
    out: DescribeClusterTracksMessage = {}  # type: ignore[typeddict-item]
    child_maintenance_track_name = el.find("MaintenanceTrackName")
    if child_maintenance_track_name is not None:
        out["maintenance_track_name"] = str(child_maintenance_track_name.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
