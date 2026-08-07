"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteClusterSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class DeleteClusterSnapshotMessage(TypedDict, closed=True):
    snapshot_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier of the manual snapshot to be deleted.</p> <p>Constraints: Must be the name of an existing snapshot that is in the <code>available</code>, <code>failed</code>, or <code>cancelled</code> state.</p>"""
    snapshot_cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.</p> <p>Constraints: Must be the name of valid cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteClusterSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "snapshot_identifier" in value:
        pairs.append(
            (f"{key_prefix}SnapshotIdentifier", str(value["snapshot_identifier"]))
        )
    if "snapshot_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}SnapshotClusterIdentifier",
                str(value["snapshot_cluster_identifier"]),
            )
        )


def deserialize_query(el: Element) -> DeleteClusterSnapshotMessage:
    out: DeleteClusterSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_snapshot_identifier = el.find("SnapshotIdentifier")
    if child_snapshot_identifier is not None:
        out["snapshot_identifier"] = str(child_snapshot_identifier.text or "")
    child_snapshot_cluster_identifier = el.find("SnapshotClusterIdentifier")
    if child_snapshot_cluster_identifier is not None:
        out["snapshot_cluster_identifier"] = str(
            child_snapshot_cluster_identifier.text or ""
        )
    return out
