"""Generated from Smithy shape ``com.amazonaws.backup#CreateBackupPlanOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.advanced_backup_settings
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.timestamp


class CreateBackupPlanOutput(TypedDict):
    backup_plan_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The ID of the backup plan.</p>"""
    backup_plan_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, <code>arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50</code>.</p>"""
    creation_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time that a backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    version_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.</p>"""
    advanced_backup_settings: NotRequired[
        "aws_sdk_backup.types.advanced_backup_settings.AdvancedBackupSettings"
    ]
    """<p>The settings for a resource type. This option is only available for Windows Volume Shadow Copy Service (VSS) backup jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackupPlanOutput) -> dict:
    out: dict = {}
    if "backup_plan_id" in value:
        out["BackupPlanId"] = value["backup_plan_id"]
    if "backup_plan_arn" in value:
        out["BackupPlanArn"] = value["backup_plan_arn"]
    if "creation_date" in value:
        import aws_sdk_backup.types.timestamp

        out["CreationDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "advanced_backup_settings" in value:
        import aws_sdk_backup.types.advanced_backup_settings

        out["AdvancedBackupSettings"] = (
            aws_sdk_backup.types.advanced_backup_settings.serialize_json(
                value["advanced_backup_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateBackupPlanOutput:
    out: CreateBackupPlanOutput = {}  # type: ignore[typeddict-item]
    if "BackupPlanId" in data:
        out["backup_plan_id"] = data["BackupPlanId"]
    if "BackupPlanArn" in data:
        out["backup_plan_arn"] = data["BackupPlanArn"]
    if "CreationDate" in data:
        import aws_sdk_backup.types.timestamp

        out["creation_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    if "AdvancedBackupSettings" in data:
        import aws_sdk_backup.types.advanced_backup_settings

        out["advanced_backup_settings"] = (
            aws_sdk_backup.types.advanced_backup_settings.deserialize_json(
                data["AdvancedBackupSettings"]
            )
        )
    return out
