"""Generated from Smithy shape ``com.amazonaws.backup#StartBackupJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.boolean2
    import capo_backup.types.string
    import capo_backup.types.timestamp


class StartBackupJobOutput(TypedDict, closed=True):
    backup_job_id: NotRequired["capo_backup.types.string.string"]
    """<p>Uniquely identifies a request to Backup to back up a resource.</p>"""
    recovery_point_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p> <i>Note: This field is only returned for Amazon EFS and Advanced DynamoDB resources.</i> </p> <p>An ARN that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    creation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a backup job is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    is_parent: "capo_backup.types.boolean2.Boolean2"
    """<p>This is a returned boolean value indicating this is a parent (composite) backup job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBackupJobOutput) -> dict:
    out: dict = {}
    if "backup_job_id" in value:
        out["BackupJobId"] = value["backup_job_id"]
    if "recovery_point_arn" in value:
        out["RecoveryPointArn"] = value["recovery_point_arn"]
    if "creation_date" in value:
        import capo_backup.types.timestamp

        out["CreationDate"] = capo_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    out["IsParent"] = value.get("is_parent", False)
    return out


def deserialize_json(data: dict) -> StartBackupJobOutput:
    out: StartBackupJobOutput = {}  # type: ignore[typeddict-item]
    if "BackupJobId" in data:
        out["backup_job_id"] = data["BackupJobId"]
    if "RecoveryPointArn" in data:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    if "CreationDate" in data:
        import capo_backup.types.timestamp

        out["creation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if "IsParent" in data:
        out["is_parent"] = data["IsParent"]
    else:
        out["is_parent"] = False
    return out
