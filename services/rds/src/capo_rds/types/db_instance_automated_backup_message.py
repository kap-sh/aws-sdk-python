"""Generated from Smithy shape ``com.amazonaws.rds#DBInstanceAutomatedBackupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_instance_automated_backup_list
    import capo_rds.types.string


class DBInstanceAutomatedBackupMessage(TypedDict, closed=True):
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_instance_automated_backups: NotRequired[
        "capo_rds.types.db_instance_automated_backup_list.DBInstanceAutomatedBackupList"
    ]
    """<p>A list of <code>DBInstanceAutomatedBackup</code> instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstanceAutomatedBackupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_instance_automated_backups" in value:
        import capo_rds.types.db_instance_automated_backup_list

        capo_rds.types.db_instance_automated_backup_list.serialize_query(
            value["db_instance_automated_backups"],
            pairs,
            f"{prefix}.DBInstanceAutomatedBackups",
        )


def deserialize_query(el: Element) -> DBInstanceAutomatedBackupMessage:
    out: DBInstanceAutomatedBackupMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_instance_automated_backups = el.find("DBInstanceAutomatedBackups")
    if child_db_instance_automated_backups is not None:
        import capo_rds.types.db_instance_automated_backup_list

        out["db_instance_automated_backups"] = (
            capo_rds.types.db_instance_automated_backup_list.deserialize_query(
                child_db_instance_automated_backups
            )
        )
    return out
