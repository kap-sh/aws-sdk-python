"""Generated from Smithy shape ``com.amazonaws.backup#DeleteBackupPlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.string
    import capo_backup.types.timestamp


class DeleteBackupPlanOutput(TypedDict, closed=True):
    backup_plan_id: NotRequired["capo_backup.types.string.string"]
    """<p>Uniquely identifies a backup plan.</p>"""
    backup_plan_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, <code>arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50</code>.</p>"""
    deletion_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time (UTC). The value of <code>DeletionDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    version_id: NotRequired["capo_backup.types.string.string"]
    """<p>Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBackupPlanOutput) -> dict:
    out: dict = {}
    if "backup_plan_id" in value:
        out["BackupPlanId"] = value["backup_plan_id"]
    if "backup_plan_arn" in value:
        out["BackupPlanArn"] = value["backup_plan_arn"]
    if "deletion_date" in value:
        import capo_backup.types.timestamp

        out["DeletionDate"] = capo_backup.types.timestamp.serialize_json(
            value["deletion_date"]
        )
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> DeleteBackupPlanOutput:
    out: DeleteBackupPlanOutput = {}  # type: ignore[typeddict-item]
    if "BackupPlanId" in data:
        out["backup_plan_id"] = data["BackupPlanId"]
    if "BackupPlanArn" in data:
        out["backup_plan_arn"] = data["BackupPlanArn"]
    if "DeletionDate" in data:
        import capo_backup.types.timestamp

        out["deletion_date"] = capo_backup.types.timestamp.deserialize_json(
            data["DeletionDate"]
        )
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    return out
