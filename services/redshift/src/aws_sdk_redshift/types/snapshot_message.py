"""Generated from Smithy shape ``com.amazonaws.redshift#SnapshotMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.snapshot_list
    import aws_sdk_redshift.types.string


class SnapshotMessage(TypedDict):
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    snapshots: NotRequired["aws_sdk_redshift.types.snapshot_list.SnapshotList"]
    """<p>A list of <a>Snapshot</a> instances. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "snapshots" in value:
        import aws_sdk_redshift.types.snapshot_list

        aws_sdk_redshift.types.snapshot_list.serialize_query(
            value["snapshots"], pairs, f"{prefix}.Snapshots"
        )


def deserialize_query(el: Element) -> SnapshotMessage:
    out: SnapshotMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_snapshots = el.find("Snapshots")
    if child_snapshots is not None:
        import aws_sdk_redshift.types.snapshot_list

        out["snapshots"] = aws_sdk_redshift.types.snapshot_list.deserialize_query(
            child_snapshots
        )
    return out
