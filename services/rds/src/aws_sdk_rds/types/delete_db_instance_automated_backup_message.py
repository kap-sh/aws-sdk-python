"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBInstanceAutomatedBackupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class DeleteDBInstanceAutomatedBackupMessage(TypedDict):
    dbi_resource_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The identifier for the source DB instance, which can't be changed and which is unique to an Amazon Web Services Region.</p>"""
    db_instance_automated_backups_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the automated backups to delete, for example, <code>arn:aws:rds:us-east-1:123456789012:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE</code>.</p> <p>This setting doesn't apply to RDS Custom.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBInstanceAutomatedBackupMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dbi_resource_id" in value:
        pairs.append((f"{prefix}.DbiResourceId", str(value["dbi_resource_id"])))
    if "db_instance_automated_backups_arn" in value:
        pairs.append(
            (
                f"{prefix}.DBInstanceAutomatedBackupsArn",
                str(value["db_instance_automated_backups_arn"]),
            )
        )


def deserialize_query(el: Element) -> DeleteDBInstanceAutomatedBackupMessage:
    out: DeleteDBInstanceAutomatedBackupMessage = {}  # type: ignore[typeddict-item]
    child_dbi_resource_id = el.find("DbiResourceId")
    if child_dbi_resource_id is not None:
        out["dbi_resource_id"] = str(child_dbi_resource_id.text or "")
    child_db_instance_automated_backups_arn = el.find("DBInstanceAutomatedBackupsArn")
    if child_db_instance_automated_backups_arn is not None:
        out["db_instance_automated_backups_arn"] = str(
            child_db_instance_automated_backups_arn.text or ""
        )
    return out
