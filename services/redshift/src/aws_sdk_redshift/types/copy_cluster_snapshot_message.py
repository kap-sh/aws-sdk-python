"""Generated from Smithy shape ``com.amazonaws.redshift#CopyClusterSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string


class CopyClusterSnapshotMessage(TypedDict, closed=True):
    source_snapshot_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier for the source snapshot.</p> <p>Constraints:</p> <ul> <li> <p>Must be the identifier for a valid automated snapshot whose state is <code>available</code>.</p> </li> </ul>"""
    source_snapshot_cluster_identifier: NotRequired[
        "aws_sdk_redshift.types.string.String"
    ]
    """<p>The identifier of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.</p> <p>Constraints:</p> <ul> <li> <p>Must be the identifier for a valid cluster.</p> </li> </ul>"""
    target_snapshot_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier given to the new manual snapshot.</p> <p>Constraints:</p> <ul> <li> <p>Cannot be null, empty, or blank.</p> </li> <li> <p>Must contain from 1 to 255 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Must be unique for the Amazon Web Services account that is making the request.</p> </li> </ul>"""
    manual_snapshot_retention_period: NotRequired[
        "aws_sdk_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely. </p> <p>The value must be either -1 or an integer between 1 and 3,653.</p> <p>The default value is -1.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CopyClusterSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_snapshot_identifier" in value:
        pairs.append(
            (
                f"{prefix}.SourceSnapshotIdentifier",
                str(value["source_snapshot_identifier"]),
            )
        )
    if "source_snapshot_cluster_identifier" in value:
        pairs.append(
            (
                f"{prefix}.SourceSnapshotClusterIdentifier",
                str(value["source_snapshot_cluster_identifier"]),
            )
        )
    if "target_snapshot_identifier" in value:
        pairs.append(
            (
                f"{prefix}.TargetSnapshotIdentifier",
                str(value["target_snapshot_identifier"]),
            )
        )
    if "manual_snapshot_retention_period" in value:
        pairs.append(
            (
                f"{prefix}.ManualSnapshotRetentionPeriod",
                str(value["manual_snapshot_retention_period"]),
            )
        )


def deserialize_query(el: Element) -> CopyClusterSnapshotMessage:
    out: CopyClusterSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_source_snapshot_identifier = el.find("SourceSnapshotIdentifier")
    if child_source_snapshot_identifier is not None:
        out["source_snapshot_identifier"] = str(
            child_source_snapshot_identifier.text or ""
        )
    child_source_snapshot_cluster_identifier = el.find(
        "SourceSnapshotClusterIdentifier"
    )
    if child_source_snapshot_cluster_identifier is not None:
        out["source_snapshot_cluster_identifier"] = str(
            child_source_snapshot_cluster_identifier.text or ""
        )
    child_target_snapshot_identifier = el.find("TargetSnapshotIdentifier")
    if child_target_snapshot_identifier is not None:
        out["target_snapshot_identifier"] = str(
            child_target_snapshot_identifier.text or ""
        )
    child_manual_snapshot_retention_period = el.find("ManualSnapshotRetentionPeriod")
    if child_manual_snapshot_retention_period is not None:
        out["manual_snapshot_retention_period"] = int(
            child_manual_snapshot_retention_period.text or ""
        )
    return out
