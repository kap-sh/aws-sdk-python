"""Generated from Smithy shape ``com.amazonaws.redshift#ModifySnapshotCopyRetentionPeriodMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean
    import aws_sdk_redshift.types.integer
    import aws_sdk_redshift.types.string


class ModifySnapshotCopyRetentionPeriodMessage(TypedDict):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The unique identifier of the cluster for which you want to change the retention period for either automated or manual snapshots that are copied to a destination Amazon Web Services Region.</p> <p>Constraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.</p>"""
    retention_period: NotRequired["aws_sdk_redshift.types.integer.Integer"]
    """<p>The number of days to retain automated snapshots in the destination Amazon Web Services Region after they are copied from the source Amazon Web Services Region.</p> <p>By default, this only changes the retention period of copied automated snapshots. </p> <p>If you decrease the retention period for automated snapshots that are copied to a destination Amazon Web Services Region, Amazon Redshift deletes any existing automated snapshots that were copied to the destination Amazon Web Services Region and that fall outside of the new retention period.</p> <p>Constraints: Must be at least 1 and no more than 35 for automated snapshots. </p> <p>If you specify the <code>manual</code> option, only newly copied manual snapshots will have the new retention period. </p> <p>If you specify the value of -1 newly copied manual snapshots are retained indefinitely.</p> <p>Constraints: The number of days must be either -1 or an integer between 1 and 3,653 for manual snapshots.</p>"""
    manual: NotRequired["aws_sdk_redshift.types.boolean.Boolean"]
    """<p>Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifySnapshotCopyRetentionPeriodMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "retention_period" in value:
        pairs.append((f"{prefix}.RetentionPeriod", str(value["retention_period"])))
    if "manual" in value:
        pairs.append((f"{prefix}.Manual", "true" if value["manual"] else "false"))


def deserialize_query(el: Element) -> ModifySnapshotCopyRetentionPeriodMessage:
    out: ModifySnapshotCopyRetentionPeriodMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_retention_period = el.find("RetentionPeriod")
    if child_retention_period is not None:
        out["retention_period"] = int(child_retention_period.text or "")
    child_manual = el.find("Manual")
    if child_manual is not None:
        out["manual"] = (child_manual.text or "").lower() == "true"
    return out
