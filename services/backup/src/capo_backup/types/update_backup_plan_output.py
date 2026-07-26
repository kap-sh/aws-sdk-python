"""Generated from Smithy shape ``com.amazonaws.backup#UpdateBackupPlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.advanced_backup_settings
    import capo_backup.types.arn
    import capo_backup.types.scan_settings
    import capo_backup.types.string
    import capo_backup.types.timestamp


class UpdateBackupPlanOutput(TypedDict, closed=True):
    backup_plan_id: NotRequired["capo_backup.types.string.string"]
    """<p>Uniquely identifies a backup plan.</p>"""
    backup_plan_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, <code>arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50</code>.</p>"""
    creation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time a backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    version_id: NotRequired["capo_backup.types.string.string"]
    """<p>Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version Ids cannot be edited.</p>"""
    advanced_backup_settings: NotRequired[
        "capo_backup.types.advanced_backup_settings.AdvancedBackupSettings"
    ]
    """<p>Contains a list of <code>BackupOptions</code> for each resource type.</p>"""
    scan_settings: NotRequired["capo_backup.types.scan_settings.ScanSettings"]
    """<p>Contains your scanning configuration for the backup plan and includes the Malware scanner, your selected resources, and scanner role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackupPlanOutput) -> dict:
    out: dict = {}
    if "backup_plan_id" in value:
        out["BackupPlanId"] = value["backup_plan_id"]
    if "backup_plan_arn" in value:
        out["BackupPlanArn"] = value["backup_plan_arn"]
    if "creation_date" in value:
        import capo_backup.types.timestamp

        out["CreationDate"] = capo_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "advanced_backup_settings" in value:
        import capo_backup.types.advanced_backup_settings

        out["AdvancedBackupSettings"] = (
            capo_backup.types.advanced_backup_settings.serialize_json(
                value["advanced_backup_settings"]
            )
        )
    if "scan_settings" in value:
        import capo_backup.types.scan_settings

        out["ScanSettings"] = capo_backup.types.scan_settings.serialize_json(
            value["scan_settings"]
        )
    return out


def deserialize_json(data: dict) -> UpdateBackupPlanOutput:
    out: UpdateBackupPlanOutput = {}  # type: ignore[typeddict-item]
    if "BackupPlanId" in data:
        out["backup_plan_id"] = data["BackupPlanId"]
    if "BackupPlanArn" in data:
        out["backup_plan_arn"] = data["BackupPlanArn"]
    if "CreationDate" in data:
        import capo_backup.types.timestamp

        out["creation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    if "AdvancedBackupSettings" in data:
        import capo_backup.types.advanced_backup_settings

        out["advanced_backup_settings"] = (
            capo_backup.types.advanced_backup_settings.deserialize_json(
                data["AdvancedBackupSettings"]
            )
        )
    if "ScanSettings" in data:
        import capo_backup.types.scan_settings

        out["scan_settings"] = capo_backup.types.scan_settings.deserialize_json(
            data["ScanSettings"]
        )
    return out
