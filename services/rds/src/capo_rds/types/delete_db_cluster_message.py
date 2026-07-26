"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.boolean_optional
    import capo_rds.types.string


class DeleteDBClusterMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The DB cluster identifier for the DB cluster to be deleted. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match an existing DBClusterIdentifier.</p> </li> </ul>"""
    skip_final_snapshot: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Specifies whether to skip the creation of a final DB cluster snapshot before RDS deletes the DB cluster. If you set this value to <code>true</code>, RDS doesn't create a final DB cluster snapshot. If you set this value to <code>false</code> or don't specify it, RDS creates a DB cluster snapshot before it deletes the DB cluster. By default, this parameter is disabled, so RDS creates a final DB cluster snapshot.</p> <note> <p>If <code>SkipFinalSnapshot</code> is disabled, you must specify a value for the <code>FinalDBSnapshotIdentifier</code> parameter.</p> </note>"""
    final_db_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The DB cluster snapshot identifier of the new DB cluster snapshot created when <code>SkipFinalSnapshot</code> is disabled.</p> <note> <p>If you specify this parameter and also skip the creation of a final DB cluster snapshot with the <code>SkipFinalShapshot</code> parameter, the request results in an error.</p> </note> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens</p> </li> </ul>"""
    delete_automated_backups: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to remove automated backups immediately after the DB cluster is deleted. This parameter isn't case-sensitive. The default is to remove automated backups immediately after the DB cluster is deleted, unless the Amazon Web Services Backup policy specifies a point-in-time restore rule.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "skip_final_snapshot" in value:
        pairs.append(
            (
                f"{prefix}.SkipFinalSnapshot",
                "true" if value["skip_final_snapshot"] else "false",
            )
        )
    if "final_db_snapshot_identifier" in value:
        pairs.append(
            (
                f"{prefix}.FinalDBSnapshotIdentifier",
                str(value["final_db_snapshot_identifier"]),
            )
        )
    if "delete_automated_backups" in value:
        pairs.append(
            (
                f"{prefix}.DeleteAutomatedBackups",
                "true" if value["delete_automated_backups"] else "false",
            )
        )


def deserialize_query(el: Element) -> DeleteDBClusterMessage:
    out: DeleteDBClusterMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_skip_final_snapshot = el.find("SkipFinalSnapshot")
    if child_skip_final_snapshot is not None:
        out["skip_final_snapshot"] = (
            child_skip_final_snapshot.text or ""
        ).lower() == "true"
    child_final_db_snapshot_identifier = el.find("FinalDBSnapshotIdentifier")
    if child_final_db_snapshot_identifier is not None:
        out["final_db_snapshot_identifier"] = str(
            child_final_db_snapshot_identifier.text or ""
        )
    child_delete_automated_backups = el.find("DeleteAutomatedBackups")
    if child_delete_automated_backups is not None:
        out["delete_automated_backups"] = (
            child_delete_automated_backups.text or ""
        ).lower() == "true"
    return out
