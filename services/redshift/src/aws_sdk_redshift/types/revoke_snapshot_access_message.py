"""Generated from Smithy shape ``com.amazonaws.redshift#RevokeSnapshotAccessMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class RevokeSnapshotAccessMessage(TypedDict):
    snapshot_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of the snapshot that the account can no longer access.</p>"""
    snapshot_arn: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the snapshot associated with the message to revoke access.</p>"""
    snapshot_cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.</p>"""
    account_with_restore_access: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of the Amazon Web Services account that can no longer restore the specified snapshot.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RevokeSnapshotAccessMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_identifier" in value:
        pairs.append(
            (f"{prefix}.SnapshotIdentifier", str(value["snapshot_identifier"]))
        )
    if "snapshot_arn" in value:
        pairs.append((f"{prefix}.SnapshotArn", str(value["snapshot_arn"])))
    if "snapshot_cluster_identifier" in value:
        pairs.append(
            (
                f"{prefix}.SnapshotClusterIdentifier",
                str(value["snapshot_cluster_identifier"]),
            )
        )
    if "account_with_restore_access" in value:
        pairs.append(
            (
                f"{prefix}.AccountWithRestoreAccess",
                str(value["account_with_restore_access"]),
            )
        )


def deserialize_query(el: Element) -> RevokeSnapshotAccessMessage:
    out: RevokeSnapshotAccessMessage = {}  # type: ignore[typeddict-item]
    child_snapshot_identifier = el.find("SnapshotIdentifier")
    if child_snapshot_identifier is not None:
        out["snapshot_identifier"] = str(child_snapshot_identifier.text or "")
    child_snapshot_arn = el.find("SnapshotArn")
    if child_snapshot_arn is not None:
        out["snapshot_arn"] = str(child_snapshot_arn.text or "")
    child_snapshot_cluster_identifier = el.find("SnapshotClusterIdentifier")
    if child_snapshot_cluster_identifier is not None:
        out["snapshot_cluster_identifier"] = str(
            child_snapshot_cluster_identifier.text or ""
        )
    child_account_with_restore_access = el.find("AccountWithRestoreAccess")
    if child_account_with_restore_access is not None:
        out["account_with_restore_access"] = str(
            child_account_with_restore_access.text or ""
        )
    return out
