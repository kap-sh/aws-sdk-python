"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.boolean_optional
    import capo_rds.types.string


class DeleteDBInstanceMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The DB instance identifier for the DB instance to be deleted. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the name of an existing DB instance.</p> </li> </ul>"""
    skip_final_snapshot: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Specifies whether to skip the creation of a final DB snapshot before deleting the instance. If you enable this parameter, RDS doesn't create a DB snapshot. If you don't enable this parameter, RDS creates a DB snapshot before the DB instance is deleted. By default, skip isn't enabled, and the DB snapshot is created.</p> <note> <p>If you don't enable this parameter, you must specify the <code>FinalDBSnapshotIdentifier</code> parameter.</p> </note> <p>When a DB instance is in a failure state and has a status of <code>failed</code>, <code>incompatible-restore</code>, or <code>incompatible-network</code>, RDS can delete the instance only if you enable this parameter.</p> <p>If you delete a read replica or an RDS Custom instance, you must enable this setting.</p> <p>This setting is required for RDS Custom.</p>"""
    final_db_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The <code>DBSnapshotIdentifier</code> of the new <code>DBSnapshot</code> created when the <code>SkipFinalSnapshot</code> parameter is disabled.</p> <note> <p>If you enable this parameter and also enable SkipFinalShapshot, the command results in an error.</p> </note> <p>This setting doesn't apply to RDS Custom.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 letters or numbers.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Can't be specified when deleting a read replica.</p> </li> </ul>"""
    delete_automated_backups: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to remove automated backups immediately after the DB instance is deleted. This parameter isn't case-sensitive. The default is to remove automated backups immediately after the DB instance is deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBInstanceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "skip_final_snapshot" in value:
        pairs.append(
            (
                f"{key_prefix}SkipFinalSnapshot",
                "true" if value["skip_final_snapshot"] else "false",
            )
        )
    if "final_db_snapshot_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}FinalDBSnapshotIdentifier",
                str(value["final_db_snapshot_identifier"]),
            )
        )
    if "delete_automated_backups" in value:
        pairs.append(
            (
                f"{key_prefix}DeleteAutomatedBackups",
                "true" if value["delete_automated_backups"] else "false",
            )
        )


def deserialize_query(el: Element) -> DeleteDBInstanceMessage:
    out: DeleteDBInstanceMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
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
