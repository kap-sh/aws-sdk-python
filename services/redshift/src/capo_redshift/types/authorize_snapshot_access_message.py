"""Generated from Smithy shape ``com.amazonaws.redshift#AuthorizeSnapshotAccessMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class AuthorizeSnapshotAccessMessage(TypedDict, closed=True):
    snapshot_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the snapshot the account is authorized to restore.</p>"""
    snapshot_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the snapshot to authorize access to.</p>"""
    snapshot_cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the cluster the snapshot was created from.</p> <ul> <li> <p> <i>If the snapshot to access doesn't exist and the associated IAM policy doesn't allow access to all (*) snapshots</i> - This parameter is required. Otherwise, permissions aren't available to check if the snapshot exists.</p> </li> <li> <p> <i>If the snapshot to access exists</i> - This parameter isn't required. Redshift can retrieve the cluster identifier and use it to validate snapshot authorization.</p> </li> </ul>"""
    account_with_restore_access: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the Amazon Web Services account authorized to restore the specified snapshot.</p> <p>To share a snapshot with Amazon Web Services Support, specify amazon-redshift-support.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthorizeSnapshotAccessMessage, pairs: list[tuple[str, str]], prefix: str
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


def deserialize_query(el: Element) -> AuthorizeSnapshotAccessMessage:
    out: AuthorizeSnapshotAccessMessage = {}  # type: ignore[typeddict-item]
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
