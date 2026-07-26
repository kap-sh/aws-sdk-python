"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterSnapshotCopyStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integer
    import capo_redshift.types.long
    import capo_redshift.types.string


class ClusterSnapshotCopyStatus(TypedDict, closed=True):
    destination_region: NotRequired["capo_redshift.types.string.String"]
    """<p>The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.</p>"""
    retention_period: NotRequired["capo_redshift.types.long.Long"]
    """<p>The number of days that automated snapshots are retained in the destination region after they are copied from a source region.</p>"""
    manual_snapshot_retention_period: NotRequired["capo_redshift.types.integer.Integer"]
    """<p>The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely. </p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>"""
    snapshot_copy_grant_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the snapshot copy grant.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterSnapshotCopyStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "destination_region" in value:
        pairs.append((f"{prefix}.DestinationRegion", str(value["destination_region"])))
    if "retention_period" in value:
        pairs.append((f"{prefix}.RetentionPeriod", str(value["retention_period"])))
    if "manual_snapshot_retention_period" in value:
        pairs.append(
            (
                f"{prefix}.ManualSnapshotRetentionPeriod",
                str(value["manual_snapshot_retention_period"]),
            )
        )
    if "snapshot_copy_grant_name" in value:
        pairs.append(
            (f"{prefix}.SnapshotCopyGrantName", str(value["snapshot_copy_grant_name"]))
        )


def deserialize_query(el: Element) -> ClusterSnapshotCopyStatus:
    out: ClusterSnapshotCopyStatus = {}  # type: ignore[typeddict-item]
    child_destination_region = el.find("DestinationRegion")
    if child_destination_region is not None:
        out["destination_region"] = str(child_destination_region.text or "")
    child_retention_period = el.find("RetentionPeriod")
    if child_retention_period is not None:
        out["retention_period"] = int(child_retention_period.text or "")
    child_manual_snapshot_retention_period = el.find("ManualSnapshotRetentionPeriod")
    if child_manual_snapshot_retention_period is not None:
        out["manual_snapshot_retention_period"] = int(
            child_manual_snapshot_retention_period.text or ""
        )
    child_snapshot_copy_grant_name = el.find("SnapshotCopyGrantName")
    if child_snapshot_copy_grant_name is not None:
        out["snapshot_copy_grant_name"] = str(child_snapshot_copy_grant_name.text or "")
    return out
