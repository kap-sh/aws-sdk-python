"""Generated from Smithy shape ``com.amazonaws.redshift#SnapshotCopyGrantMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.snapshot_copy_grant_list
    import aws_sdk_redshift.types.string


class SnapshotCopyGrantMessage(TypedDict):
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <code>DescribeSnapshotCopyGrant</code> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p> <p>Constraints: You can specify either the <b>SnapshotCopyGrantName</b> parameter or the <b>Marker</b> parameter, but not both. </p>"""
    snapshot_copy_grants: NotRequired[
        "aws_sdk_redshift.types.snapshot_copy_grant_list.SnapshotCopyGrantList"
    ]
    """<p>The list of <code>SnapshotCopyGrant</code> objects.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotCopyGrantMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "snapshot_copy_grants" in value:
        import aws_sdk_redshift.types.snapshot_copy_grant_list

        aws_sdk_redshift.types.snapshot_copy_grant_list.serialize_query(
            value["snapshot_copy_grants"], pairs, f"{prefix}.SnapshotCopyGrants"
        )


def deserialize_query(el: Element) -> SnapshotCopyGrantMessage:
    out: SnapshotCopyGrantMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_snapshot_copy_grants = el.find("SnapshotCopyGrants")
    if child_snapshot_copy_grants is not None:
        import aws_sdk_redshift.types.snapshot_copy_grant_list

        out["snapshot_copy_grants"] = (
            aws_sdk_redshift.types.snapshot_copy_grant_list.deserialize_query(
                child_snapshot_copy_grants
            )
        )
    return out
