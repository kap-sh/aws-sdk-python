"""Generated from Smithy shape ``com.amazonaws.redshift#SnapshotErrorMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class SnapshotErrorMessage(TypedDict, closed=True):
    snapshot_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>A unique identifier for the snapshot returning the error.</p>"""
    snapshot_cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>A unique identifier for the cluster.</p>"""
    failure_code: NotRequired["capo_redshift.types.string.String"]
    """<p>The failure code for the error.</p>"""
    failure_reason: NotRequired["capo_redshift.types.string.String"]
    """<p>The text message describing the error.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotErrorMessage, pairs: list[tuple[str, str]], prefix: str
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
    if "failure_code" in value:
        pairs.append((f"{key_prefix}FailureCode", str(value["failure_code"])))
    if "failure_reason" in value:
        pairs.append((f"{key_prefix}FailureReason", str(value["failure_reason"])))


def deserialize_query(el: Element) -> SnapshotErrorMessage:
    out: SnapshotErrorMessage = {}  # type: ignore[typeddict-item]
    child_snapshot_identifier = el.find("SnapshotIdentifier")
    if child_snapshot_identifier is not None:
        out["snapshot_identifier"] = str(child_snapshot_identifier.text or "")
    child_snapshot_cluster_identifier = el.find("SnapshotClusterIdentifier")
    if child_snapshot_cluster_identifier is not None:
        out["snapshot_cluster_identifier"] = str(
            child_snapshot_cluster_identifier.text or ""
        )
    child_failure_code = el.find("FailureCode")
    if child_failure_code is not None:
        out["failure_code"] = str(child_failure_code.text or "")
    child_failure_reason = el.find("FailureReason")
    if child_failure_reason is not None:
        out["failure_reason"] = str(child_failure_reason.text or "")
    return out
