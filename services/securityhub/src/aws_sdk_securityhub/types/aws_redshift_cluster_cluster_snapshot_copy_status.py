"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterClusterSnapshotCopyStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsRedshiftClusterClusterSnapshotCopyStatus(TypedDict):
    destination_region: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The destination Region that snapshots are automatically copied to when cross-Region snapshot copy is enabled.</p>"""
    manual_snapshot_retention_period: NotRequired[
        "aws_sdk_securityhub.types.integer.Integer"
    ]
    """<p>The number of days that manual snapshots are retained in the destination Region after they are copied from a source Region.</p> <p>If the value is <code>-1</code>, then the manual snapshot is retained indefinitely.</p> <p>Valid values: Either <code>-1</code> or an integer between 1 and 3,653</p>"""
    retention_period: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of days to retain automated snapshots in the destination Region after they are copied from a source Region.</p>"""
    snapshot_copy_grant_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the snapshot copy grant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterClusterSnapshotCopyStatus) -> dict:
    out: dict = {}
    if "destination_region" in value:
        out["DestinationRegion"] = value["destination_region"]
    if "manual_snapshot_retention_period" in value:
        out["ManualSnapshotRetentionPeriod"] = value["manual_snapshot_retention_period"]
    if "retention_period" in value:
        out["RetentionPeriod"] = value["retention_period"]
    if "snapshot_copy_grant_name" in value:
        out["SnapshotCopyGrantName"] = value["snapshot_copy_grant_name"]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterClusterSnapshotCopyStatus:
    out: AwsRedshiftClusterClusterSnapshotCopyStatus = {}  # type: ignore[typeddict-item]
    if "DestinationRegion" in data:
        out["destination_region"] = data["DestinationRegion"]
    if "ManualSnapshotRetentionPeriod" in data:
        out["manual_snapshot_retention_period"] = data["ManualSnapshotRetentionPeriod"]
    if "RetentionPeriod" in data:
        out["retention_period"] = data["RetentionPeriod"]
    if "SnapshotCopyGrantName" in data:
        out["snapshot_copy_grant_name"] = data["SnapshotCopyGrantName"]
    return out
