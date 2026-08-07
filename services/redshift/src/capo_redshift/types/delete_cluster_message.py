"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.boolean
    import capo_redshift.types.integer_optional
    import capo_redshift.types.string


class DeleteClusterMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the cluster to be deleted.</p> <p>Constraints:</p> <ul> <li> <p>Must contain lowercase characters.</p> </li> <li> <p>Must contain from 1 to 63 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    skip_final_cluster_snapshot: NotRequired["capo_redshift.types.boolean.Boolean"]
    """<p>Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If <code>true</code>, a final cluster snapshot is not created. If <code>false</code>, a final cluster snapshot is created before the cluster is deleted. </p> <note> <p>The <i>FinalClusterSnapshotIdentifier</i> parameter must be specified if <i>SkipFinalClusterSnapshot</i> is <code>false</code>.</p> </note> <p>Default: <code>false</code> </p>"""
    final_cluster_snapshot_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, <i>SkipFinalClusterSnapshot</i> must be <code>false</code>. </p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 alphanumeric characters.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    final_cluster_snapshot_retention_period: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p> <p>The default value is -1.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "skip_final_cluster_snapshot" in value:
        pairs.append(
            (
                f"{key_prefix}SkipFinalClusterSnapshot",
                "true" if value["skip_final_cluster_snapshot"] else "false",
            )
        )
    if "final_cluster_snapshot_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}FinalClusterSnapshotIdentifier",
                str(value["final_cluster_snapshot_identifier"]),
            )
        )
    if "final_cluster_snapshot_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}FinalClusterSnapshotRetentionPeriod",
                str(value["final_cluster_snapshot_retention_period"]),
            )
        )


def deserialize_query(el: Element) -> DeleteClusterMessage:
    out: DeleteClusterMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_skip_final_cluster_snapshot = el.find("SkipFinalClusterSnapshot")
    if child_skip_final_cluster_snapshot is not None:
        out["skip_final_cluster_snapshot"] = (
            child_skip_final_cluster_snapshot.text or ""
        ).lower() == "true"
    child_final_cluster_snapshot_identifier = el.find("FinalClusterSnapshotIdentifier")
    if child_final_cluster_snapshot_identifier is not None:
        out["final_cluster_snapshot_identifier"] = str(
            child_final_cluster_snapshot_identifier.text or ""
        )
    child_final_cluster_snapshot_retention_period = el.find(
        "FinalClusterSnapshotRetentionPeriod"
    )
    if child_final_cluster_snapshot_retention_period is not None:
        out["final_cluster_snapshot_retention_period"] = int(
            child_final_cluster_snapshot_retention_period.text or ""
        )
    return out
