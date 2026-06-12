"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterAutomatedBackupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_cluster_automated_backup_list
    import aws_sdk_rds.types.string


class DBClusterAutomatedBackupMessage(TypedDict):
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The pagination token provided in the previous request. If this parameter is specified the response includes only records beyond the marker, up to <code>MaxRecords</code>.</p>"""
    db_cluster_automated_backups: NotRequired[
        "aws_sdk_rds.types.db_cluster_automated_backup_list.DBClusterAutomatedBackupList"
    ]
    """<p>A list of <code>DBClusterAutomatedBackup</code> backups.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterAutomatedBackupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_cluster_automated_backups" in value:
        import aws_sdk_rds.types.db_cluster_automated_backup_list

        aws_sdk_rds.types.db_cluster_automated_backup_list.serialize_query(
            value["db_cluster_automated_backups"],
            pairs,
            f"{prefix}.DBClusterAutomatedBackups",
        )


def deserialize_query(el: Element) -> DBClusterAutomatedBackupMessage:
    out: DBClusterAutomatedBackupMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_cluster_automated_backups = el.find("DBClusterAutomatedBackups")
    if child_db_cluster_automated_backups is not None:
        import aws_sdk_rds.types.db_cluster_automated_backup_list

        out["db_cluster_automated_backups"] = (
            aws_sdk_rds.types.db_cluster_automated_backup_list.deserialize_query(
                child_db_cluster_automated_backups
            )
        )
    return out
